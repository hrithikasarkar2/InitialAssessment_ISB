import requests
import pandas as pd

# Define the base URL and years range
base_url = "https://www.teaboard.gov.in/WEEKLYPRICES/"
years = range(2008, 2024)

# Define a function to scrape and consolidate the data
def scrape_tea_prices():
    # Create an empty list to store the scraped data
    tea_data = []

    # Loop through the years
    for year in years:
        # Construct the URL for the current year
        url = base_url + str(year)

        # Send a GET request to the URL
        response = requests.get(url)

        # Read the HTML table into a DataFrame
        tables = pd.read_html(response.text)
        df = tables[0]

        # Extract the required columns
        df = df.iloc[1:, :3]  # Exclude the header row and keep only the first 3 columns
        df.columns = ["week", "location", "average_price"]  # Rename the columns

        # Append the data to the list
        tea_data.append(df)

        # Print a message indicating the completion of scraping for the current year
        print(f"Scraping completed for {year}")

    # Concatenate the dataframes into a single dataframe
    consolidated_data = pd.concat(tea_data, ignore_index=True)

    # Convert the week column to the desired date format (DD-MM-YYYY)
    consolidated_data["week"] = pd.to_datetime(consolidated_data["week"]).dt.strftime("%d-%m-%Y")

    return consolidated_data


# Call the scrape_tea_prices() function
consolidated_data = scrape_tea_prices()

# Save the consolidated data to a CSV file
csv_file = "tea_prices.csv"
consolidated_data.to_csv(csv_file, index=False)

# Print a message indicating the completion of the script
print(f"Data scraping and consolidation completed. The CSV file '{csv_file}' has been saved.")

