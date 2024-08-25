# File 1: FX Data Fetching and Processing

import os
import requests
import pandas as pd
from datetime import datetime

API_KEY = 'K8G9ER9C53SYNGKQ'
CURRENCY_PAIRS = [
    ('USD', 'EUR'),
    ('USD', 'GBP'),
    ('USD', 'JPY'),
    ('EUR', 'GBP'),
    ('EUR', 'JPY')
]
OUTPUT_DIR_RAW = 'data/raw_fx_data/'
OUTPUT_DIR_PROCESSED = 'data/processed_data/'

os.makedirs(OUTPUT_DIR_RAW, exist_ok=True)
os.makedirs(OUTPUT_DIR_PROCESSED, exist_ok=True)

def fetch_fx_data(from_currency, to_currency):
    url = f'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol={from_currency}&to_symbol={to_currency}&apikey={API_KEY}&datatype=csv'
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f'{OUTPUT_DIR_RAW}{from_currency}_{to_currency}_fx.csv'
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    else:
        return None

def process_fx_data(file_path):
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    df = df[['open', 'high', 'low', 'close']].sort_index()
    processed_file_path = f'{OUTPUT_DIR_PROCESSED}{os.path.basename(file_path)}'
    df = df.loc[df.index >= pd.Timestamp(datetime.now()) - pd.DateOffset(years=10)]
    df.to_csv(processed_file_path)
    return processed_file_path

def main():
    for from_currency, to_currency in CURRENCY_PAIRS:
        raw_file = fetch_fx_data(from_currency, to_currency)
        if raw_file:
            process_fx_data(raw_file)

if __name__ == '__main__':
    main()
