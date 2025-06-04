import pandas as pd
from google.oauth2 import service_account
from pandas_gbq import to_gbq
import os

# Load credentials
credentials = service_account.Credentials.from_service_account_file('gcp_bigquery.json')

# Load your crypto data
df = pd.read_csv('data/processed/crypto_historical_prices.csv')

# Define destination
project_id = "sanguine-method-430206-q8"
dataset_table = "state_of_the_economy.crypto_prices"

# Upload
to_gbq(df, dataset_table, project_id=project_id, if_exists='replace', credentials=credentials)

print("Data uploaded to BigQuery")