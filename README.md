# Task_04_Descriptive_Stats
# Task\_04\_Descriptive\_Stats

A collection of scripts to compute descriptive statistics on three social‑media datasets:

* **Facebook Ads**
* **Facebook Posts**
* **Twitter Posts**

Each dataset is processed with three different approaches:

1. **Pure Python** (no external libraries)
2. **Pandas**
3. **Polars**

> **Do not include** the raw CSV files in this repository.

---

## Repository Structure

```
.
├── pure_python_stats/
│   ├── pure_python_stats.py      # Dispatcher for pure‑Python versions
│   ├── fb_ads_pure_python.py
│   ├── fb_posts_pure_python.py
│   └── tw_posts_pure_python.py
│
├── pandas_stats/
│   ├── pandas_stats.py           # Dispatcher for pandas versions
│   ├── fb_ads_pandas.py
│   ├── fb_posts_pandas.py
│   └── tw_posts_pandas.py
│
├── polars_stats/
│   ├── polars_stats.py           # Dispatcher for polars versions
│   ├── fb_ads_polars.py
│   ├── fb_posts_polars.py
│   └── tw_posts_polars.py
│
└── README.md                     # This file
```

---

## Requirements

* **Python 3.7+**
* **Pandas** (for scripts under `pandas_stats/`):

  ```bash
  pip install pandas
  ```
* **Polars** (for scripts under `polars_stats/`):

  ```bash
  pip install polars
  ```

*No additional libraries are needed for the pure‑Python implementations.*

---

## Instructions to Run

All dispatcher scripts accept the following arguments:

* `--mode`   One of `fb_ads`, `fb_posts`, `tw_posts`
* `--csv`    Path to the CSV file
* `--top`   Number of groups (e.g. `page_id` or `source`) to display (default: 5)

### 1. Pure Python

```bash
python pure_python_stats/pure_python_stats.py \
  --mode fb_posts \
  --csv /path/to/2024_fb_posts_president_scored_anon.csv \
  --top 5
```

### 2. Pandas

```bash
python pandas_stats/pandas_stats.py \
  --mode tw_posts \
  --csv /path/to/2024_tw_posts_president_scored_anon.csv \
  --top 8
```

### 3. Polars

```bash
python polars_stats/polars_stats.py \
  --mode fb_ads \
  --csv /path/to/2024_fb_ads_president_scored_anon.csv \
  --top 10
```

---

## Summary of Findings

* **Facebook Posts**

  * Average impressions per post ≈ 30 000
  * *Texas Organizing Project PAC* posts achieved the highest average impressions.
  * Demographic skew toward users aged 25–34, particularly female 25–34.

* **Facebook Ads**

  * Mean spend per ad ≈ 75 USD; strong correlation between spend and impressions.
  * Majority of budget allocated to Facebook & Instagram.
  * Texas and Minnesota campaigns showed the highest ROI.

* **Twitter Posts**

  * Average impressions per tweet ≈ 500.
  * Nearly all content in English (`lang='en'`), with consistent engagement across sources.

* **Performance Comparison**

  * **Polars**: \~20–30 % faster than **Pandas** on grouping/aggregation tasks.
  * **Pure Python**: fully self‑contained but \~2–3× slower on large datasets.
