# 📜 Quotes Web Scraper (Life Quotes)

## 📸 Sample Output
![Life Quotes Output](https://raw.githubusercontent.com/MohsinKhalidDar/web-scraping-quotes/main/screenshots/output_preview.png)

This project scrapes quotes from **https://quotes.toscrape.com**, filters quotes
tagged with **"life"**, and saves them into a clean CSV file.

The project is implemented as a **Jupyter Notebook** and demonstrates a complete
web-scraping pipeline: fetching data, handling pagination, retries, parsing HTML,
filtering content, and exporting structured data.

---


## 🚀 Features
- Pagination scraping (unknown number of pages)
- Retry logic for network failures
- User-Agent handling
- Raw HTML storage for reproducibility
- Data extraction using BeautifulSoup
- Clean CSV output using Pandas

---

## 🛠 Tech Stack
- Python
- Requests
- BeautifulSoup
- Pandas
- Jupyter Notebook

---

## 📂 Project Structure
web-scraping-quotes/
│

├── quotes_scraper.ipynb

├── requirements.txt

├── README.md

├── scraped_data/

│ └── quotes1.html, quotes2.html, ...

├── cleaned_data/

│ └── life_quotes.csv


---

## ▶ How to Run the Jupyter Notebook

1️⃣ Clone the Repository

git clone https://github.com/MohsinKhalidDar/web-scraping-quotes.git

cd web-scraping-quotes

ls


2️⃣ Create a Virtual Environment(Optional) 
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Launch Jupyter Notebook
jupyter notebook

5️⃣ Run the Notebook

Open quotes_scraper.ipynb

Run all cells from top to bottom using:

Shift + Enter
 
