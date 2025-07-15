#!/usr/bin/env python
"""
Polars-based descriptive statistics for the Facebook-posts dataset.
Requires: pip install polars
"""
import polars as pl

def fb_posts_polars(CSV_FILE):

    df = pl.read_csv(CSV_FILE)

    # ── Global describe ───────────────────────────────────────────────────────────
    print("\n=== GLOBAL describe() ===")
    print(df.describe())

    # ── Top 5 value counts for string columns ─────────────────────────────────────
    print("\n=== VALUE COUNTS (top 5) ===")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            out = (
                df.select(col).to_series()
                .value_counts()
                .sort("count", descending=True)
                .head(5)
            )
            print(f"\n{col}:\n{out}")

    # ── Grouped statistics (numeric means) ────────────────────────────────────────
    numeric_types = (
        pl.Int8, pl.Int16, pl.Int32, pl.Int64,
        pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
        pl.Float32, pl.Float64
    )
    num_cols = [c for c in df.columns if df[c].dtype in numeric_types]

    if "page_id" in df.columns:
        print("\n=== GROUPED BY page_id (numeric means, first 5 rows) ===")
        result = (
            df.group_by("page_id")
            .agg([pl.col(c).mean().alias(f"{c}_mean") for c in num_cols])
            .head()
        )
        print(result)

    if {"page_id", "ad_id"}.issubset(df.columns):
        print("\n=== GROUPED BY (page_id, ad_id) (numeric means, first 5) ===")
        result = (
            df.group_by(["page_id", "ad_id"])
            .agg([pl.col(c).mean().alias(f"{c}_mean") for c in num_cols])
            .head()
        )
        print(result)
