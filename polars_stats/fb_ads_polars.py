import polars as pl

def fb_ads_polars(csv_file):
    # Load dataset
    df = pl.read_csv(csv_file, infer_schema_length=1000)

    # Global describe
    print("\n=== GLOBAL describe() ===")
    print(df.describe())

    # Value counts for string columns
    print("\n=== VALUE COUNTS (Top 5 for string columns) ===")
    for col in df.columns:
        if df.schema[col] == pl.Utf8:
            vc = df.select(pl.col(col)).to_series().value_counts().sort("count", descending=True).head(5)
            print(f"\n{col}:\n{vc}")

    # Unique values
    print("\n=== UNIQUE VALUE COUNTS ===")
    for col in df.columns:
        try:
            nunique = df.select(pl.col(col).n_unique()).item()
            print(f"{col}: {nunique}")
        except Exception as e:
            print(f"{col}: Could not compute unique values ({e})")

    # Identify numeric columns
    numeric_types = (
        pl.Int8, pl.Int16, pl.Int32, pl.Int64,
        pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
        pl.Float32, pl.Float64
    )

    num_cols = [col for col, dtype in df.schema.items() if dtype in numeric_types]

    # Grouped by page_id
    if "page_id" in df.columns:
        print("\n=== GROUPED BY page_id (numeric means) ===")
        grouped_page = df.group_by("page_id").agg([
            pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
        ])
        print(grouped_page)

    # Grouped by (page_id, ad_id)
    if "page_id" in df.columns and "ad_id" in df.columns:
        print("\n=== GROUPED BY (page_id, ad_id) (numeric means) ===")
        grouped_page_ad = df.group_by(["page_id", "ad_id"]).agg([
            pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
        ])
        print(grouped_page_ad)
