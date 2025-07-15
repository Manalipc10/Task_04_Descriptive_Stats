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
        stats[col] = {
            "count": n,
            "mean": mean,
            "min": minimum,
            "max": maximum,
            "std": std
        }
    return stats

def compute_non_numeric_stats(rows, non_numeric_cols, top=5):
    stats = {}
    for col in non_numeric_cols:
        vals = [r[col] for r in rows if r[col].strip() != ""]
        cnt = len(vals)
        uniq = len(set(vals))
        freq = Counter(vals).most_common(top)
        stats[col] = {
            "count": cnt,
            "unique": uniq,
            "top": freq
        }
    return stats

def print_overall(rows):
    print("\n=== OVERALL DATASET ANALYSIS ===")
    numeric, non_numeric = detect_column_types(rows)
    num_stats = compute_numeric_stats(rows, numeric)
    non_stats = compute_non_numeric_stats(rows, non_numeric)
    for c in numeric:
        s = num_stats[c]
        print(
            f"{c:30s}  count={s['count']:6d}  "
            f"mean={s['mean']:.4f}  min={s['min']:.4f}  "
            f"max={s['max']:.4f}  std={s['std']:.4f}"
        )
    for c in non_numeric:
        s = non_stats[c]
        print(
            f"{c:30s}  count={s['count']:6d}  "
            f"unique={s['unique']:6d}  top={s['top']}"
        )

def group_by(rows, keys):
    groups = defaultdict(list)
    for r in rows:
        k = tuple(r[k].strip() for k in keys)
        groups[k].append(r)
    return groups

def print_group_means(rows, group_keys, numeric_cols, top_n=5):
    groups = group_by(rows, group_keys)
    title = ", ".join(group_keys)
    print(f"\n=== GROUPED BY ({title}) — numeric means of first {top_n} groups ===")
    for i, (key, grp) in enumerate(groups.items()):
        if i >= top_n:
            break
        parts = []
        for c in numeric_cols:
            vals = [float(r[c]) for r in grp if r[c].strip() != ""]
            m = sum(vals)/len(vals) if vals else float('nan')
            parts.append(f"{c}_mean={m:.4f}")
        print(f"{', '.join(key):30s}  " + "  ".join(parts))

def analyze_fb_posts(csv_path, top_n_groups=5):
    """Importable entrypoint for FB posts CSV analysis."""
    rows = read_csv(csv_path)
    if not rows:
        print("No data found.")
        return

    # 1) overall stats
    print_overall(rows)

    # 2) group by page_id (average metrics per page)
    numeric_cols, _ = detect_column_types(rows)
    if "page_id" in rows[0]:
        print_group_means(rows, ["page_id"], numeric_cols, top_n_groups)

    # 3) (optional) group by page_id + ad_id (per‑post averages)
    if "page_id" in rows[0] and "ad_id" in rows[0]:
        print_group_means(rows, ["page_id", "ad_id"], numeric_cols, top_n_groups)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Analyze FB posts CSV")
    p.add_argument("csv_path", help="Path to your FB posts CSV file")
    p.add_argument("--top", type=int, default=5,
                   help="How many groups to display")
    args = p.parse_args()
    analyze_fb_posts(args.csv_path, args.top)
