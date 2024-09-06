import pandas as pd
import numpy as np

def count_outliers(df):
    outliers = {}
    for col in df.select_dtypes(include=[np.number]).columns:
        outliers[col] = (df[col] > df[col].quantile(0.99)).sum()
    return pd.Series(outliers)

def summary_summary(df):

    summary = df.describe().T[["count", "mean", "std", "min", "max"]]

    s = pd.DataFrame({
        "unique": pd.Series([len(df[x].value_counts()) for x in df.columns], index=df.columns),
        "null": df.isnull().sum(),
        "dtypes": df.dtypes,
        "dupe": [df.duplicated().sum() for x in df.columns],
        "outliers": count_outliers(df)
    })
    s = pd.concat([s, summary], axis=1).fillna(" ")
    s["outliers"] = [int(x) if x != " " else " " for x in s["outliers"]]
    s["count"] = [int(x) if x != " " else " " for x in s["count"]]
    return s.sort_values("dtypes")