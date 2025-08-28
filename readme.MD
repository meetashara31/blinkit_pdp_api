# 🛒 Blinkit Product Scraper (FastAPI + Tailwind UI)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)](https://fastapi.tiangolo.com/)  
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-ff69b4)](https://www.uvicorn.org/)  
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-UI-38bdf8?logo=tailwindcss)](https://tailwindcss.com/)  
[![Flowbite](https://img.shields.io/badge/Flowbite-Components-1a56db)](https://flowbite.com/)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

Here is the link to test the api > https://blinkit-api-d7dr.onrender.com/scrape-ui

## 📖 Project Overview
The **Blinkit Product Scraper (FastAPI + Tailwind UI)** is a lightweight and modern **FastAPI** project that extracts product details from Blinkit using PRID or the url of the product.  

It provides both:
- 🟢 **REST API JSON endpoints** for developers  
- 🎨 **Modern UI (Tailwind + Flowbite)** for testing directly in the browser  

---

## ✨ Features
- 🔍 Scrapeusing PRID or the url of the product  
- ⚡ Built with **FastAPI + Uvicorn** for high performance  
- 🎨 User-friendly UI with **TailwindCSS & Flowbite**  
- 📦 Clean project structure (models, scraper, templates)  
- 🛠️ Error handling with proper API responses  


---

## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git https://github.com/meetashara31/blinkit_pdp_api


2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Project

Start the FastAPI server:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload


Now visit:

🌐 UI: http://127.0.0.1:8000

📜 API Docs: http://127.0.0.1:8000/docs

🟢 Health Check: http://127.0.0.1:8000/health

📦 Example Usage
API Request
curl -X POST "http://127.0.0.1:8000/scrape" \
     -H "Content-Type: application/json" \
     -d '{"asin": "B08N5WRWNW"}'

API Response
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

🖼️ UI Preview

The UI is built using TailwindCSS + Flowbite for a clean modern look.
It lets you enter an PRID or the url of the product, test the scraper, and view results in real-time.

📌 Project Structure
├── main.py          # FastAPI app entry point
├── utils.py        # usefull functions for cleaning response
├── scraper.py       # Scraper logic
├── templates/       # Jinja2 templates for UI
│   └── index.html
├── requirements.txt # Dependencies
└── README.md        # Project documentation

🛡️ License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project.

⭐ Contributing

Contributions are welcome!
If you like this project, give it a ⭐ on GitHub to support it 🙌




