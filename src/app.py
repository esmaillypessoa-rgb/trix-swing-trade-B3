import os
import pandas as pd

from indicators import calculate_trix
from signal_engine import generate_signal
from ranking import calculate_score
from macro import macro_score
from fundamental import fundamental_score
from ai_engine import generate_analysis

DATA_DIR = "../data/raw"


def run():
    results = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            ticker = file.replace(".csv", "")
            df = pd.read_csv(f"{DATA_DIR}/{file}")

            df = calculate_trix(df)

            signal = generate_signal(df)

            # Score técnico
            if signal == "COMPRA":
                tech_score = 8
            elif signal == "VENDA":
                tech_score = 6
            else:
                tech_score = 4

            fund_score = fundamental_score()
            macro_val = macro_score()

            final_score = calculate_score(
                tech_score,
                fund_score,
                macro_val
            )

            analysis = generate_analysis(ticker, final_score, signal)

            results.append({
                "ticker": ticker,
                "signal": signal,
                "score": round(final_score, 2),
                "analysis": analysis
            })

    df_result = pd.DataFrame(results)
    df_result.sort_values(by="score", ascending=False, inplace=True)

    print("\n📊 Ranking de Ativos:\n")
    print(df_result)


if __name__ == "__main__":
    run()
