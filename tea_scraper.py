import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Tea Board of India website
base_url = "https://www.teaboard.gov.in/WEEKLYPRICES/"

# Function to scrape data for a given year
def scrape_data(year):
    url = f"{base_url}{year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")

    city_names = []
    for row in rows[0].find_all("th")[1:]:
        city_name = row.get_text(strip=True)
        if city_name:
            city_names.append(city_name)

    for row in rows[1:]:
        cells = row.find_all("td")
        week = cells[0].text.strip()

        for i, cell in enumerate(cells[1:], start=1):
            location = city_names[i - 1]
            average_price = cell.text.strip()
            if location == "mjunction" and average_price == "":
                average_price = cells[i - 1].text.strip()
            data.append([week, location, average_price])

    return data

# Scrape data for all available years
years = range(2008, 2024)
consolidated_data = []
for year in years:
    consolidated_data.extend(scrape_data(year))

# Convert the data into a DataFrame
df = pd.DataFrame(consolidated_data, columns=["Week", "Location", "Average_Price"])

# Save the DataFrame to a CSV file
df.to_csv("tea_prices.csv", index=False)

print("Data saved to tea_prices.csv")