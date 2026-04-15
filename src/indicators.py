def calculate_trix(df, period=8):
    ema1 = df['Close'].ewm(span=period).mean()
    ema2 = ema1.ewm(span=period).mean()
    ema3 = ema2.ewm(span=period).mean()

    df['TRIX'] = ema3.pct_change() * 100
    df['TRIX_MA'] = df['TRIX'].rolling(window=period).mean()

    return df
