#!/usr/bin/env python

import polars as pl

def tw_posts_polars(CSV_FILE):
    df = pl.read_csv(CSV_FILE)

    print("\n=== GLOBAL describe() ===")
    print(df.describe())

    print("\n=== VALUE COUNTS (top 5) ===")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            vc = (
                df.select(col).to_series()
                .value_counts()
                .sort("count", descending=True)
                .head(5)
            )
            print(f"\n{col}:\n{vc}")
