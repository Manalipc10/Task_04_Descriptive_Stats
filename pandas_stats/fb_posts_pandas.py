#!/usr/bin/env python
"""
Pandas-based descriptive statistics for the Facebook-posts dataset.
"""

import pandas as pd

def fb_posts_pandas(CSV_FILE):

    df = pd.read_csv(CSV_FILE)

    # ── Global describe ───────────────────────────────────────────────────────────
    print("\n=== GLOBAL describe() ===")
    print(df.describe(include="all").transpose())

    # ── Top 5 value counts for object columns ─────────────────────────────────────
    print("\n=== VALUE COUNTS (top 5) ===")
    for col in df.select_dtypes(include="object"):
        print(f"\n{col}:")
        print(df[col].value_counts(dropna=False).head())

    # ── Grouped statistics ────────────────────────────────────────────────────────
    if "page_id" in df.columns:
        print("\n=== GROUPED BY page_id (describe) ===")
        print(df.groupby("page_id").describe().transpose())

    if {"page_id", "ad_id"}.issubset(df.columns):
        print("\n=== GROUPED BY (page_id, ad_id) (first 3 groups) ===")
        grouped = df.groupby(["page_id", "ad_id"]).describe()
        for i, (idx, block) in enumerate(grouped.groupby(level=0)):
            if i == 3:
                break
            print(f"\npage_id={idx}  (showing first rows)")
            print(block.head())
