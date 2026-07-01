import pandas as pd


REQUIRED_COLUMNS = ["close"]


def load_dataset(path):
    try:
        df = pd.read_csv(path)

    except FileNotFoundError:
        raise FileNotFoundError("Input file not found.")

    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty.")

    except Exception:
        raise ValueError("Invalid CSV format.")

    if df.empty:
        raise ValueError("Dataset is empty.")

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    return df