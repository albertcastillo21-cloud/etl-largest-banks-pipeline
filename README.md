# ETL Pipeline: Scraping Top 10 Banks by Market Cap

## Description
This project scrapes a Wikipedia web page to extract a table containing the world's top 10 banks ranked by market capitalization in USD. The data is then transformed by converting the market cap values into multiple currencies (GBP, EUR, and INR) and loaded into both a CSV file and a SQLite database for further analysis.

## Technologies Used
- `pandas` — data manipulation and transformation
- `numpy` — numerical operations and rounding
- `requests` — HTTP requests to fetch web page content
- `beautifulsoup4` — HTML parsing and web scraping
- `sqlite3` — local database storage
- `sqlalchemy` — database engine support
- `lxml` — HTML/XML parser
- `datetime` — timestamp generation for logging

## Data Source
Wikipedia archive snapshot (September 2023):
https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks

## Project Structure
```
├── banks_project.py    # Core ETL functions: extract, transform, load, query, and logging
├── main.py             # Entry point: defines variables and executes the ETL pipeline
├── exchange_rate.csv   # CSV file containing currency exchange rates (USD to GBP, EUR, INR)
├── requirements.txt    # All required libraries to run this project successfully
```

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/albertcastillo21-cloud/etl-largest-banks-pipeline.git
cd etl-largest-banks-pipeline
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install required libraries:
```bash
pip install -r requirements.txt
```

4. Run the pipeline:
```bash
python main.py
```

The pipeline will extract the data, transform it, save it to a CSV file, load it into a SQLite database, and run example queries. Progress is logged to `code_log.txt`.

## Query Examples
```sql
-- All banks with market cap in all currencies
SELECT * FROM Largest_banks;

-- Average market cap in GBP
SELECT AVG(MC_GBP_Billion) FROM Largest_banks;

-- Top 5 banks by name
SELECT Name FROM Largest_banks LIMIT 5;
```

## What I Learned
- How to structure a production-ready ETL pipeline with separated concerns (extract, transform, load)
- How to parse HTML tables using BeautifulSoup and understand HTML structure to scrape data efficiently
- How to apply currency conversion transformations across multiple columns using pandas and numpy
- How to load transformed data into both CSV and SQLite using pandas
- How to implement a logging system to track pipeline execution progress
