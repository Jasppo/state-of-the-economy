# Load packages ============================

from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file ============
load_dotenv()

# Read environment variables ==================
user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
host = os.getenv('PG_HOST')
port = os.getenv('PG_PORT')
db = os.getenv('PG_DB')

# Create connection ================
connection_str = f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(connection_str)

# Read in data =================
df = pd.read_csv('data/processed/crypto_historical_prices.csv')

# Insert into PostgreSQL ============
df.to_sql('crypto_prices', engine, if_exists='replace', index=False)
print("Data inserted into PostgreSQL table: crypto_prices")