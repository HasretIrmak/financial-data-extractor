# gui.py

import tkinter as tk
from tkinter import messagebox
from data_fetcher import fetch_stock_data, fetch_crypto_data

# Function to fetch stock data
def fetch_stock_data_gui():
    fetch_stock_data()
    messagebox.showinfo("Success", "Stock data has been successfully fetched!")

# Function to fetch crypto data
def fetch_crypto_data_gui():
    fetch_crypto_data()
    messagebox.showinfo("Success", "Crypto data has been successfully fetched!")

# Main window
root = tk.Tk()
root.title("Investing Data Scraper")
root.geometry("600x400")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Investing Data Scraper", font=("Arial", 20, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Stock data fetch button
stock_button = tk.Button(root, text="Fetch Stock Data", font=("Arial", 14), bg="#4CAF50", fg="white", command=fetch_stock_data_gui)
stock_button.pack(pady=10, padx=20, fill="x")

# Crypto data fetch button
crypto_button = tk.Button(root, text="Fetch Crypto Data", font=("Arial", 14), bg="#2196F3", fg="white", command=fetch_crypto_data_gui)
crypto_button.pack(pady=10, padx=20, fill="x")

# Start the main loop
root.mainloop()
