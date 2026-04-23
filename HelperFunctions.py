import os
import pandas as pd
import numpy as np


"""Purpose:
        Various functions that will be called in other python scripts to streamline processing
        
"""


def csv_to_df(csv_file):
    df = pd.read_csv(csv_file)
    return df


def df_col_stats(df: pd.DataFrame, col: str) -> tuple[float, float, float]:
    series = df[col]

    minn = series.min() #nans are excluded when converted to series dtype
    maxx = series.max()
    std = series.std()

    return float(minn), float(maxx), float(std)

