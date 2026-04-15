def generate_signal(df):
    last = df.iloc[-1]

    if last['TRIX'] > last['TRIX_MA'] and last['TRIX'] > 0:
        return "COMPRA"
    elif last['TRIX'] < last['TRIX_MA'] and last['TRIX'] < 0:
        return "VENDA"
    else:
        return "NEUTRO"
