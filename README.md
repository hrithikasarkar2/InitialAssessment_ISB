# Tea Prices Web Scraper

This is a Python script that scrapes the "WEEKLY AVERAGE PRICES OF TOTAL TEA SOLD AT INDIAN AUCTION" table from the Tea Board of India website for all available years (2008-2023). The scraped data is then consolidated and saved in a CSV file.

## Usage

1. Install the dependencies by running the following command:

pip install -r requirements.txt

2. Run the script using the following command:

python tea_scraper.py


3. After running the script, a CSV file named `tea_prices.csv` will be generated in the same directory. The file contains the consolidated tea price data with three columns: week, location, and average_price.

## Additional Notes

- The script utilizes the Requests library for making HTTP requests and the Pandas library for data manipulation and consolidation.
- The script scrapes the data for each year from 2008 to 2023, so it may take some time to complete the scraping process.
- The CSV file will be overwritten each time the script is run.

