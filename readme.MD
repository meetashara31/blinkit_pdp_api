# 🛒 Blinkit Product Scraper (FastAPI + Tailwind UI)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)  
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

A modern **FastAPI-based API** to fetch structured **Blinkit product details** using either a **Product URL** or **Product ID (prid)**.  
Get details like product name, price, MRP, availability, images, description, ingredients, and more in clean JSON format.  

---

## ✨ Features
- 🔍 Input: Blinkit Product URL or Product ID (`prid`)  
- 📦 Output: Structured JSON with product info  
- ⚡ Built with **FastAPI** (super fast, async-ready)  
- 🛡️ Robust error handling for invalid inputs  
- 📖 Interactive Swagger docs at `/docs`  
- 🔗 Easy integration into data pipelines, dashboards, or e-commerce tools  

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/blinkit-product-scraper.git
cd blinkit-product-scraper
2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the API
uvicorn main:app --reload


API will be live at 👉 http://127.0.0.1:8000

📌 Usage
🟢 Swagger UI

Visit: http://127.0.0.1:8000/docs

🟢 Example Request (cURL / Postman)

POST /extract

{
  "url_or_prid": "490670"
}

🟢 Example Response
{
  "product_id": "490670",
  "product_name": "Colgate Visible White O2 Whitening Toothpaste (25 g)",
  "merchant_id": 30560,
  "mrp": 160,
  "price": 136,
  "availability": "available",
  "images": ["..."],
  "others": {"Description": "...", "Ingredients": "..."}
}

🛠️ Tech Stack

FastAPI
 – web framework

Uvicorn
 – ASGI server

Python
 – core language