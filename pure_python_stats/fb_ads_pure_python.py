#!/usr/bin/env python3
import csv
import math
from collections import Counter, defaultdict

def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def is_float_string(s):
    try:
        float(s)
        return True
    except:
        return False

def detect_column_types(rows):
    cols = rows[0].keys()
    numeric, non_numeric = [], []
    for c in cols:
        vals = [r[c].strip() for r in rows if r[c].strip() != ""]
        if vals and all(is_float_string(v) for v in vals):
            numeric.append(c)
        else:
            non_numeric.append(c)
    return numeric, non_numeric

def compute_numeric_stats(rows, numeric_cols):
    stats = {}
    for col in numeric_cols:
        vals = [float(r[col]) for r in rows if r[col].strip() != ""]
        n = len(vals)
        if n == 0:
            stats[col] = None
            continue
        mean = sum(vals) / n
        minimum, maximum = min(vals), max(vals)
        std = math.sqrt(sum((x - mean) ** 2 for x in vals) / n)
        stats[col] = {"count": n, "mean": mean, "min": minimum, "max": maximum, "std": std}
    return stats

def compute_non_numeric_stats(rows, non_numeric_cols, top=5):
    stats = {}
    for col in non_numeric_cols:
        vals = [r[col] for r in rows if r[col].strip() != ""]
        cnt = len(vals)
        uniq = len(set(vals))
        freq = Counter(vals).most_common(top)
        stats[col] = {"count": cnt, "unique": uniq, "top": freq}
    return stats

def print_overall(rows):
    print("\n=== OVERALL DATASET ANALYSIS ===")
    numeric, non_numeric = detect_column_types(rows)
    num_stats = compute_numeric_stats(rows, numeric)
    non_stats = compute_non_numeric_stats(rows, non_numeric)
    for c in numeric:
        s = num_stats[c]
        print(f"{c:20s}  count={s['count']:5d}  mean={s['mean']:.4f} "
              f"min={s['min']:.4f}  max={s['max']:.4f}  std={s['std']:.4f}")
    for c in non_numeric:
        s = non_stats[c]
        print(f"{c:20s}  count={s['count']:5d}  unique={s['unique']:5d}  top={s['top']}")

def group_by(rows, keys):
    groups = defaultdict(list)
    for r in rows:
        k = tuple(r[k].strip() for k in keys)
        groups[k].append(r)
    return groups

def print_group_means(rows, group_keys, numeric_cols, top_n=5):
    groups = group_by(rows, group_keys)
    header = ", ".join(group_keys)
    print(f"\n=== GROUPED BY ({header}) — numeric means of first {top_n} groups ===")
    for i, (key, grp) in enumerate(groups.items()):
        if i >= top_n: break
        means = []
        for c in numeric_cols:
            vals = [float(r[c]) for r in grp if r[c].strip() != ""]
            m = sum(vals)/len(vals) if vals else float('nan')
            means.append(f"{c}_mean={m:.4f}")
        print(f"{', '.join(key):30s}  " + "  ".join(means))

def analyze_fb_ads(csv_path, top_n_groups=5):
    """Top‑level function you can import and call."""
    rows = read_csv(csv_path)
    if not rows:
        print("No data found.")
        return
    # overall stats
    print_overall(rows)
    # grouped stats
    numeric_cols, _ = detect_column_types(rows)
    if "page_id" in rows[0]:
        print_group_means(rows, ["page_id"], numeric_cols, top_n_groups)
    if "page_id" in rows[0] and "ad_id" in rows[0]:
        print_group_means(rows, ["page_id", "ad_id"], numeric_cols, top_n_groups)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Analyze FB ads CSV")
    p.add_argument("csv_path", help="Path to the CSV file")
    p.add_argument("--top", type=int, default=5, help="How many groups to show")
    args = p.parse_args()
    analyze_fb_ads(args.csv_path, args.top)
