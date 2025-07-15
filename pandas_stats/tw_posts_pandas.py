#!/usr/bin/env python
import pandas as pd

def tw_posts_pandas(CSV_FILE):
    df = pd.read_csv(CSV_FILE)

    print("\n=== GLOBAL describe() ===")
    print(df.describe(include="all").transpose())

    print("\n=== VALUE COUNTS (top 5) ===")
    for col in df.select_dtypes(include="object"):
        print(f"\n{col}:\n{df[col].value_counts(dropna=False).head()}")
