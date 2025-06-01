# Load packages ============================

import requests
import pandas as pd
from datetime import datetime

# Function: Get historical crypto prices ==========================

def get_historical_prices(coin_id, vs_currency='usd', days=365):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        'vs_currency': vs_currency,
        'days': days,
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    df = pd.DataFrame(prices, columns = ['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit = 'ms').dt.date
    df = df[['date', 'price']]
    df['coin'] = coin_id
    return df

if __name__ == "__main__":
    btc_df = get_historical_prices('bitcoin')
    eth_df = get_historical_prices('ethereum')
    combined = pd.concat([btc_df, eth_df])
    combined.to_csv('data/processed/crypto_historical_prices.csv', index = False)
    print("Saved historical crypto prices to data/processed/crypto_historical_prices.csv")