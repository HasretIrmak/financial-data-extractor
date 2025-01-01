# financial-data-extractor

It is a Python-based project that allows you to scrape stock and cryptocurrency data from [Investing.com](https://www.investing.com). This tool enables you to easily gather financial data and save it in CSV format for further analysis.

## Features

- **Stock Data Fetching**: Retrieves the latest stock prices and their changes from Investing.com.
- **Cryptocurrency Data Fetching**: Retrieves the latest cryptocurrency prices and their changes.
- **Graphical User Interface (GUI)**: A simple and intuitive GUI built with Tkinter to initiate data scraping tasks.
- **CSV Output**: The scraped data is saved in two CSV files: `stocks_data.csv` for stock data and `crypto_data.csv` for cryptocurrency data.

## Requirements

Before running this project, you need to install the following dependencies:

- **requests**: For making HTTP requests to fetch the data.
- **beautifulsoup4**: For parsing HTML data and extracting the required information.
- **pandas**: For organizing and saving the scraped data into CSV files.
- **tkinter**: For creating the graphical user interface (GUI).

You can install the required dependencies by running:

```bash
pip install -r requirements.txt


