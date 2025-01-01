# data_fetcher.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch stock data
def fetch_stock_data():
    url_stocks = "https://www.investing.com/equities"
    response_stocks = requests.get(url_stocks)
    soup_stocks = BeautifulSoup(response_stocks.text, 'html.parser')

    stocks_data = []
    for row in soup_stocks.find_all('tr', class_='js-all-symbols'):
        try:
            name = row.find('td', class_='instrument').text.strip()
            price = row.find('td', class_='price').text.strip()
            change = row.find('td', class_='priceChange').text.strip()
            stocks_data.append([name, price, change])
        except AttributeError:
            continue

    stocks_df = pd.DataFrame(stocks_data, columns=["Name", "Price", "Change"])
    stocks_df.to_csv("stocks_data.csv", index=False)

# Function to fetch crypto data
def fetch_crypto_data():
    url_crypto = "https://www.investing.com/crypto"
    response_crypto = requests.get(url_crypto)
    soup_crypto = BeautifulSoup(response_crypto.text, 'html.parser')

    crypto_data = []
    for row in soup_crypto.find_all('tr', class_='js-all-symbols'):
        try:
            name = row.find('td', class_='instrument').text.strip()
            price = row.find('td', class_='price').text.strip()
            change = row.find('td', class_='priceChange').text.strip()
            crypto_data.append([name, price, change])
        except AttributeError:
            continue

    crypto_df = pd.DataFrame(crypto_data, columns=["Name", "Price", "Change"])
    crypto_df.to_csv("crypto_data.csv", index=False)
