import requests
import pandas as pd
from datetime import datetime, date
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
engine = create_engine(
    f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
)

def get_latest_price(coin_id, vs_currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': vs_currency
    }
    response = requests.get(url, params=params)
    price = response.json()[coin_id][vs_currency]
    return {'date': date.today(), 'price': price, 'coin': coin_id}

def main():
    btc = get_latest_price('bitcoin')
    eth = get_latest_price('ethereum')
    df = pd.DataFrame([btc, eth])

    # Check for duplicates before inserting
    existing = pd.read_sql("SELECT date, coin FROM crypto_prices", engine)
    df = df.merge(existing, on=['date', 'coin'], how='left', indicator=True)
    df = df[df['_merge'] == 'left_only'].drop(columns=['_merge'])

    if not df.empty:
        df.to_sql('crypto_prices', engine, if_exists='append', index=False)
        print("Added today's prices.")
    else:
        print("Prices for today already exist. Skipping insert.")

if __name__ == "__main__":
    main()

