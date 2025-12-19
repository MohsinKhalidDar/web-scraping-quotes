# Imports & Setup

import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import time
from requests.exceptions import RequestException

# Create Required Folders
os.makedirs("scraped_data", exist_ok=True)
os.makedirs("cleaned_data", exist_ok=True)

# Fetch Pages & Save HTML (SCRAPING)
headers = {
    "User-Agent": "Mozilla/5.0"
}

page_count = 1
MAX_RETRIES = 3

while True:
    url = f"https://quotes.toscrape.com/page/{page_count}/"
    print(f"Fetching page {page_count}...")

    success = False

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                success = True
                break
        except RequestException as e:
            print(f"Attempt {attempt} failed:", e)
            time.sleep(2)

    if not success:
        print(f"Skipping page {page_count} after {MAX_RETRIES} retries")
        page_count += 1
        continue

    soup = BeautifulSoup(res.text, "lxml")
    quotes = soup.select("div.quote")

    if not quotes:
        print("No more valid pages. Stopping.")
        break

    with open(f"scraped_data/quotes{page_count}.html", "w", encoding="utf-8") as f:
        f.write(res.text)

    print(f"Downloaded data from page {page_count}")

    page_count += 1
    time.sleep(1)
    
# Read Saved HTML Files
files = sorted(os.listdir("scraped_data"))
files


# Extract “Life” Quotes from All Pages

life_quotes = []

for file in files:
    if file.startswith("quotes") and file.endswith(".html"):
        print(f"Processing {file}")

        with open(f"scraped_data/{file}", "r", encoding="utf-8") as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, "lxml")
        all_quotes = soup.select("div.quote")

        for q in all_quotes:
            tags = [tag.get_text(strip=True) for tag in q.select(".tags .tag")]

            if "life" in tags:
                text = q.select_one("span.text").get_text(strip=True)
                author = q.select_one("small.author").get_text(strip=True)
                life_quotes.append([text, author])

print("Total life quotes collected:", len(life_quotes))


# Convert to DataFrame

df = pd.DataFrame(life_quotes, columns=["Quote", "Author"])
df.head()

# Save to CSV

df.to_csv("cleaned_data/life_quotes.csv", index=False, encoding="utf-8")
print("Saved to cleaned_data/life_quotes.csv")


# Sanity Check

df.tail()
