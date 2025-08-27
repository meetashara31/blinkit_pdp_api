import jmespath
import re
from curl_cffi import requests
from config import *
def smart_cast(value: str):
    # Try to convert numbers
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value 
def extract_product_id(value: str) -> str:
    # Case 1: Direct product ID (only digits)
    if value.isdigit():
        return value
    
    # Case 2: Extract from Blinkit URL
    match = re.search(r"/prid/(\d+)", value)
    if match:
        return match.group(1)

    raise ValueError("Invalid input: product ID not found")

def extract_first(paths,data):
    for path in paths:
        value = jmespath.search(path, data)
        if value:
            return value
    return None

def extract_json(prid):
    response = requests.post(
        f'https://blinkit.com/v1/layout/product/{prid}',
        headers=headers,
        impersonate='chrome101'
    )

    return response.json()