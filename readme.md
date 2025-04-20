# 🍽️ Zomato Gen AI Internship Assignment: Restaurant Data Scraper & RAG-based Chatbot

## 📌 Overview

This project implements an end-to-end Generative AI solution combining **web scraping** and a **Retrieval Augmented Generation (RAG)** chatbot to answer natural language queries about restaurants.

- **Built using:** Python
- **Runs on:** Standard CPU (no specialized hardware)
- **Libraries:** `BeautifulSoup`, `requests`, `LangChain`, `transformers`, `sentence-transformers`, `FAISS`, `Gradio`

---

## 🏗️ System Architecture

The solution is divided into four components:

1. **Web Scraper:** Scrapes data from 5–10 restaurant websites  
2. **Knowledge Base:** Preprocesses, embeds, and indexes data for retrieval  
3. **RAG Chatbot:** Uses Hugging Face models and LangChain to answer queries  
4. **User Interface:** Built with Gradio for interactive querying  

---

## 🔍 1. Web Scraper

**Objective:** Extract restaurant data from text-based websites.

### ✅ Features Extracted:
- Restaurant name & location
- Menu items: name, description, price, tags (e.g., vegetarian, gluten-free)
- Operating hours
- Contact information
- Special features (spice level, allergens)

### 🛠 Tools Used:
- `BeautifulSoup`, `requests`
- HTML parsing with custom logic for each site
- JSON schema for output

### 📁 Output: `restaurants.json`
```json
{
  "restaurant_name": "The Original",
  "location": "123 Main St, Denver, CO",
  "menu": [
    {
      "item_name": "Spicy Veggie Curry",
      "description": "A flavorful curry with fresh vegetables",
      "price": "$12.99",
      "tags": ["vegetarian", "vegan"],
      "spice_level": "medium"
    }
  ],
  "operating_hours": "Mon-Fri: 10 AM - 10 PM",
  "contact": "Phone: 123-456-7890, Email: info@..."
}


/project
├── scraper.py               # Web scraper script
├── knowledge_base.py        # Embedding and FAISS indexing
├── chatbot.py               # LangChain RAG chatbot setup
├── app.py                   # Gradio interface
├── restaurants.json         # Scraped restaurant data
├── vector_store/            # FAISS index files
└── README.md                # Project documentation

## Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the Chatbot
bash
Copy
Edit
python app.py
