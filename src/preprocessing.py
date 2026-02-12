import numpy as np
import pandas as pd

def compute_log_returns(df):
    df = df.copy()
    df["log_return"] = np.log(df["price"]).diff()
    return df.dropna()
