# State of the Economy: Real-Time Data Engineering Pipeline for Monitoring the Global & U.S. Economy

**State of the Economy** is a full-stack data engineering project that brings together real-time and historical economic data to track trends in housing, cost of living, interest rates, inflation, stock markets, and the crypto economy.

This project is built with production-grade tools to simulate what a modern data engineering pipeline looks like in industry — from ingestion to analytics and visualization.

---

## Project Goals

- Ingest real-time and batch data from reliable economic APIs and sources  
- Clean, transform, and store data in a scalable cloud warehouse  
- Automate data pipelines using Apache Airflow  
- Perform trend analysis and aggregations using SQL and dbt  
- Visualize key indicators and insights with Tableau or Power BI  

---

## Tech Stack

| Layer             | Tool / Platform                 |
| ----------------- | ------------------------------- |
| **Ingestion**     | Python, Apache Kafka, REST APIs |
| **Processing**    | Apache Spark, dbt               |
| **Storage**       | Google BigQuery (or Snowflake)  |
| **Orchestration** | Apache Airflow                  |
| **Visualization** | Tableau / Power BI              |

---

## Data Sources

- **Zillow / Redfin** — Housing prices and trends  
- **FRED (St. Louis Fed)** — CPI, interest rates, inflation  
- **CoinGecko API** — Top 100 crypto prices  
- **Yahoo Finance API / Alpha Vantage** — Stock prices and indices  
- **U.S. Census & BLS** — Income, employment, cost of living metrics  

---

## Project Modules

1. **Data Ingestion:** Real-time and batch pull from APIs  
2. **Stream Processing:** Kafka + Spark for streaming data  
3. **Data Storage:** Raw and curated layers in BigQuery  
4. **Transformations:** dbt models for clean analytics  
5. **Orchestration:** DAGs scheduled and monitored with Airflow  
6. **Dashboarding:** Interactive Tableau dashboards

---

## Key Insights Enabled

- Inflation trends vs. interest rate hikes  
- Housing affordability by ZIP and state  
- Crypto vs. S&P 500 performance  
- Cost of living and wage disparity over time  