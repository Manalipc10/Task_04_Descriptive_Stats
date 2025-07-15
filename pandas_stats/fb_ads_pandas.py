#!/usr/bin/env python
import pandas as pd

def fb_ads_pandas(CSV_FILE):
    df = pd.read_csv(CSV_FILE)

    print("\n=== GLOBAL describe() ===")
    print(df.describe(include="all").transpose())

    print("\n=== VALUE COUNTS (top 5) ===")
    for col in df.select_dtypes(include="object"):
        print(f"\n{col}:\n{df[col].value_counts(dropna=False).head()}")

    if "page_id" in df.columns:
        print("\n=== GROUPED BY page_id ===")
        print(df.groupby("page_id").describe().transpose())

    if {"page_id","ad_id"}.issubset(df.columns):
        print("\n=== GROUPED BY (page_id, ad_id) (first 3 groups) ===")
        grp = df.groupby(["page_id","ad_id"]).describe()
        for i,(idx,block) in enumerate(grp.groupby(level=0)):
            if i==3: break
            print(f"\npage_id={idx}\n{block.head()}")
