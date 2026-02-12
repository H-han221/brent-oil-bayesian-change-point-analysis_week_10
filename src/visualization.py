import matplotlib.pyplot as plt


def plot_price_series(df):
    """
    Plot Brent oil price over time.
    """
    if "date" not in df.columns or "price" not in df.columns:
        raise KeyError(
            f"Expected columns 'date' and 'price'. Found {df.columns.tolist()}"
        )

    plt.figure(figsize=(10, 4))
    plt.plot(df["date"], df["price"])
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Brent Oil Price Over Time")
    plt.tight_layout()
    plt.show()


def plot_log_returns(df):
    """
    Plot log returns over time.
    """
    if "date" not in df.columns or "log_return" not in df.columns:
        raise KeyError(
            f"Expected columns 'date' and 'log_return'. Found {df.columns.tolist()}"
        )

    plt.figure(figsize=(10, 4))
    plt.plot(df["date"], df["log_return"])
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.title("Brent Oil Log Returns")
    plt.tight_layout()
    plt.show()


def plot_volatility(df, window=30):
    """
    Plot rolling volatility of log returns.
    """
    if "log_return" not in df.columns:
        raise KeyError(
            f"'log_return' column not found. Found {df.columns.tolist()}"
        )

    volatility = df["log_return"].rolling(window).std()

    plt.figure(figsize=(10, 4))
    plt.plot(df["date"], volatility)
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.title(f"Rolling {window}-Day Volatility of Log Returns")
    plt.tight_layout()
    plt.show()
