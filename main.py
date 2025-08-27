from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

# import your existing functions
from scraper import extractor_details, extract_json
from utils import extract_product_id

app = FastAPI(
    title="Blinkit Product Scraper API",
    description="API to scrape product details from Blinkit by product ID (prid) or product URL",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


# Root endpoint
@app.get("/", response_class=HTMLResponse)
def home_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# API endpoint (already working one)
@app.post("/extract")
def extract_product(url_or_prid: str = Form(...)):
    if not url_or_prid:
        raise HTTPException(status_code=400, detail="No input provided")

    try:
        prid = extract_product_id(url_or_prid.strip())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to extract product ID: {str(e)}")

    if not prid:
        raise HTTPException(status_code=400, detail="Invalid product ID extracted")

    try:
        data = extract_json(prid=prid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch product JSON: {str(e)}")

    if not data:
        raise HTTPException(status_code=404, detail=f"No data returned for prid={prid}")

    try:
        pdp_info = extractor_details(data=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to extract product details: {str(e)}")

    if not pdp_info or not pdp_info.get("product_id"):
        raise HTTPException(status_code=404, detail="Product ID not found in extracted details")

    return pdp_info


# UI endpoint (form submit)
@app.post("/scrape-ui", response_class=HTMLResponse)
def scrape_ui(request: Request, url_or_prid: str = Form(...)):
    error = None
    data = None

    try:
        prid = extract_product_id(url_or_prid.strip())
        json_data = extract_json(prid=prid)
        data = extractor_details(data=json_data)
    except Exception as e:
        error = str(e)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "url_or_prid": url_or_prid,
        "data": data,
        "error": error
    })


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
