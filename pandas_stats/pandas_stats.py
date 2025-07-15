#!/usr/bin/env python
import pandas as pd
from fb_ads_pandas import fb_ads_pandas
from fb_posts_pandas import fb_posts_pandas
from tw_posts_pandas import tw_posts_pandas
CSV_FILE = [
    r"..\\data\\2024_fb_ads_president_scored_anon.csv",
    r"..\\data\\2024_fb_posts_president_scored_anon.csv",
    r"../data/2024_tw_posts_president_scored_anon.csv"
]

print("FB Ads President Scored Anon dataset")
fb_ads_pandas(CSV_FILE[0])

print("FB Posts President Scored Anon dataset")

fb_posts_pandas(CSV_FILE[1])

print("TW Posts President Scored Anon dataset")
tw_posts_pandas(CSV_FILE[2])



# print("\n=== GLOBAL describe() ===")
# print(df.describe(include="all").transpose())

# #fb_posts
# # ── Global describe ───────────────────────────────────────────────────────────
# print("\n=== GLOBAL describe() ===")
# print(df.describe(include="all").transpose())

# # ── Top 5 value counts for object columns ─────────────────────────────────────
# print("\n=== VALUE COUNTS (top 5) ===")
# for col in df.select_dtypes(include="object"):
#     print(f"\n{col}:")
#     print(df[col].value_counts(dropna=False).head())
# # # ── Grouped statistics ────────────────────────────────────────────────────────
# if "page_id" in df.columns:
#     print("\n=== GROUPED BY page_id (describe) ===")
#     print(df.groupby("page_id").describe().transpose())

# if {"page_id", "ad_id"}.issubset(df.columns):
#     print("\n=== GROUPED BY (page_id, ad_id) (first 3 groups) ===")
#     grouped = df.groupby(["page_id", "ad_id"]).describe()
#     for i, (idx, block) in enumerate(grouped.groupby(level=0)):
#         if i == 3:
#             break
#         print(f"\npage_id={idx}  (showing first rows)")
#         print(block.head())

# #fb_ads
# print("\n=== VALUE COUNTS (top 5) ===")
# for col in df.select_dtypes(include="object"):
#     print(f"\n{col}:\n{df[col].value_counts(dropna=False).head()}")

# if "page_id" in df.columns:
#     print("\n=== GROUPED BY page_id ===")
#     print(df.groupby("page_id").describe().transpose())

# if {"page_id","ad_id"}.issubset(df.columns):
#     print("\n=== GROUPED BY (page_id, ad_id) (first 3 groups) ===")
#     grp = df.groupby(["page_id","ad_id"]).describe()
#     for i,(idx,block) in enumerate(grp.groupby(level=0)):
#         if i==3: break
#         print(f"\npage_id={idx}\n{block.head()}")

# #tw_posts                      
# print("\n=== VALUE COUNTS (top 5) ===")
# for col in df.select_dtypes(include="object"):
#     print(f"\n{col}:\n{df[col].value_counts(dropna=False).head()}")
