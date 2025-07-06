# Web Scraper for Financial Data

import requests
from bs4 import BeautifulSoup
import csv

# URL of the financial website (example)
url = 'https://www.moneycontrol.com/stocks/marketstats/nse-mostactive-stocks/all/'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find stock data (example for illustration)
table = soup.find('table', class_='tbldata14')  # Update selector as needed

# Open CSV file to write data
with open('financial_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Name', 'Price', 'Change', 'Volume'])  # Column headers

    # Loop through rows and extract data
    for row in table.find_all('tr')[1:]:  # Skip header
        columns = row.find_all('td')
        if columns:
            name = columns[0].text.strip()
            price = columns[1].text.strip()
            change = columns[2].text.strip()
            volume = columns[3].text.strip()
            writer.writerow([name, price, change, volume])

print("Data scraped and saved to financial_data.csv")
