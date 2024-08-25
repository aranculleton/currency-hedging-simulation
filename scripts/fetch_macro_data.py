import requests
import pandas as pd
import os
from datetime import datetime

API_KEY = 'K8G9ER9C53SYNGKQ'
OUTPUT_DIR_MACRO = 'data/macro_data/'

os.makedirs(OUTPUT_DIR_MACRO, exist_ok=True)

def fetch_macro_data(function, api_key, datatype='json'):
    base_url = f"https://www.alphavantage.co/query?function={function}&apikey={api_key}&datatype={datatype}"
    response = requests.get(base_url)
    return response.json()

# Using UNEMPLOYMENT and CPI indicators which provide monthly data
indicators = {
    'Unemployment Rate': 'UNEMPLOYMENT',
    'Consumer Price Index': 'CPI'
}

def process_macro_data(df, indicator):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    # Filter data to keep only the last 10 years
    df = df.loc[df.index >= pd.Timestamp(datetime.now()) - pd.DateOffset(years=10)]
    # Resample to weekly frequency (W-FRI), forward filling any missing data
    df = df.resample('W-FRI').ffill()
    df.to_csv(f'{OUTPUT_DIR_MACRO}{indicator}.csv')

def fetch_and_process_macro_data():
    for indicator, function in indicators.items():
        data = fetch_macro_data(function, API_KEY)
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            process_macro_data(df, indicator)
        else:
            print(f"Failed to fetch {indicator} data. Response was: {data}")

def main():
    fetch_and_process_macro_data()

if __name__ == '__main__':
    main()
