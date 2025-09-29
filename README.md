# Quotes Scraper (Selenium)

A Python script that scrapes quotes from [Quotes to Scrape – Infinite Scroll](https://quotes.toscrape.com/scroll) using **Selenium**.  
The script collects quotes and authors, then saves them into a CSV file (`results.csv`).  

---

## Features

- Scrapes **quote text** and **author**.
- Set a **target number of quotes** to scrape.
- **Infinite scroll support** – dynamically loads new quotes as the page scrolls.
- Optional **respectful scraping mode**:
  - Adds a random 1–2 second delay between scraping quotes to mimic human behavior.
- Color-coded console output for better readability.
- CSV output for easy data analysis.

---

## Requirements

- Python 3.x
- Libraries:
  - `selenium`
  - `colorama`
- A compatible **Firefox WebDriver** installed (geckodriver).

Install Python dependencies with:

```bash
pip install selenium colorama
```
## Usage

1. Clone the repository or download the script.
2. Run the script:
```py
python main.py
```
3. Input the requested options:
   Target number of quotes (e.g., 50)
   Respectful scraping mode (Y / N)
4. Wait while the script scrolls and scrapes the quotes. Progress is displayed in the console.
5. Once finished, check results.csv for the collected quotes.

### Example Output (CSV)
```csv
“The world as we have created it is a process…”	Albert Einstein
```
