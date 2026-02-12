import pandas as pd


def load_brent_data(filepath: str) -> pd.DataFrame:
    """
    Load Brent oil price data.
    Expected columns: Date, Price
    """
    df = pd.read_csv(filepath)

    df.columns = df.columns.str.strip().str.lower()

    if "date" not in df.columns or "price" not in df.columns:
        raise ValueError(
            f"Expected columns 'date' and 'price'. Found {df.columns.tolist()}"
        )

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)

    return df


def load_event_data(filepath: str) -> pd.DataFrame:
    """
    Load key oil market events.
    Expected columns: date, event, category
    """
    df = pd.read_csv(filepath)

    df.columns = df.columns.str.strip().str.lower()

    required_cols = {"date", "event", "category"}
    if not required_cols.issubset(df.columns):
        raise ValueError(
            f"Missing required columns. Found {df.columns.tolist()}"
        )

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)

    return df
