import yfinance as yf
import os
from datetime import datetime, timedelta

TICKERS = [
    "PETR4.SA", "VALE3.SA", "ITUB4.SA",
    "BBDC4.SA", "WEGE3.SA"
]

OUTPUT_DIR = "../data/raw"

def fetch_data():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    end_date = datetime.today()
    start_date = end_date - timedelta(days=730)

    for ticker in TICKERS:
        print(f"Baixando {ticker}...")

        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval="1d"
        )

        df.dropna(inplace=True)

        file_name = ticker.replace(".SA", "")
        df.to_csv(f"{OUTPUT_DIR}/{file_name}.csv")

    print("✅ Dados atualizados!")

if __name__ == "__main__":
    fetch_data()
