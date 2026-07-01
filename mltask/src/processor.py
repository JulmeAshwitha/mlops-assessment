import pandas as pd


def generate_signal(df, window):
    df = df.copy()

    df["rolling_mean"] = (
        df["close"]
        .rolling(window=window, min_periods=window)
        .mean()
    )

    df["signal"] = (
        df["close"] > df["rolling_mean"]
    ).astype(int)

    df.loc[df["rolling_mean"].isna(), "signal"] = 0

    return df