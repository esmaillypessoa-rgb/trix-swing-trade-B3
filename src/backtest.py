import pandas as pd
from indicators import calculate_trix


def backtest_strategy(df):
    df = calculate_trix(df)

    position = 0
    entry_price = 0
    results = []

    for i in range(1, len(df)):
        row = df.iloc[i]

        if position == 0:
            if row['TRIX'] > row['TRIX_MA'] and row['TRIX'] > 0:
                position = 1
                entry_price = row['Close']

        elif position == 1:
            if row['TRIX'] < row['TRIX_MA']:
                exit_price = row['Close']
                profit = (exit_price - entry_price) / entry_price
                results.append(profit)
                position = 0

    return results


def performance(results):
    if len(results) == 0:
        return {}

    wins = [r for r in results if r > 0]

    return {
        "trades": len(results),
        "win_rate": len(wins) / len(results),
        "avg_return": sum(results) / len(results),
        "total_return": sum(results)
    }


if __name__ == "__main__":
    import os

    DATA_DIR = "../data/raw"

    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            print(f"\nBacktest: {file}")
            df = pd.read_csv(f"{DATA_DIR}/{file}")

            results = backtest_strategy(df)
            stats = performance(results)

            print(stats)
