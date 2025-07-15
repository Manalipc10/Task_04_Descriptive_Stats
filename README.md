# Task_04_Descriptive_Stats

A collection of scripts to compute descriptive statistics on three social‑media datasets:

* **Facebook Ads**
* **Facebook Posts**
* **Twitter Posts**

Each dataset is processed with three different approaches:

1. **Pure Python** (no external libraries)
2. **Pandas**
3. **Polars**

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

Summary of Findings

Facebook Ads

Rows processed: 246,745

Mean estimated audience size: 556,462.86

Mean estimated impressions: 45,601.53

Mean estimated spend: 1,061.29 USD

Facebook Posts

Rows processed: 19,009

Mean Likes: 2,377.70

Mean Comments: 901.58

Mean Shares: 320.54

Twitter Posts

Rows processed: 27,304

Mean viewCount: 507,084.73

Mean likeCount: 6,913.69

Mean retweetCount: 1,322.06

Run times and resource usage will vary by environment; Polars implementations are typically ~20–30% faster than Pandas on these datasets, and the pure‑Python versions, while fully self‑contained, are ~2–3× slower on large files.

Dataset Overviews

Facebook Ads (President Scored Anon)

Shape: 246,745 rows × 42 columns

Null counts: 0 nulls in key numeric columns

Unique values: page_id (4,475), ad_id (246,745), ad_creation_time (547)

Top 5 page_id by count:

4d66f5853f0365dba032a87704a634f023d15babde973bb7a284ed8cd2707b2d (55,503)

e3342051b60393770363ffc02946a0f76bc3e4155190d1f05fb0277b34bf6480 (23,988)

4ade404186269ec62d2dd7d9e0ed5f93a5f32c057516879d627ea9fbd628ef9b (14,822)

330b2f35ded2161e63fbb2b5c5bdae05bff274ff31f990c275d28ce408671ce0 (10,461)

ec8ac6dc1cddc49972de2c31b62343fe3979729ec437c3b8d6ffa8915ab1401d (9,851)

Facebook Posts (President Scored Anon)

Shape: 19,009 rows × 57 columns

Null counts: Post Views nulls (2,465), Overperforming Score nulls (0)

Unique values: Facebook_Id (21), post_id (19,009), Page Category (6)

Top 5 Facebook_Id by count:

32fc18da91029ff09bf74fe9887eace6b5d2145809d583f696e344530508b064 (9,013)

bfe51c6ac2cab17ba5c85883e76f61398031ed57e4cf62d19fd483548ebb904b (1,431)

ac24f31c4d4b3d5555065fa9558bdca4ab4b5e1379922875ae9e6e32f1d46d25 (1,231)

7f5731ac8e6959576e781064b5fa76e059200cdfc3f4e0d7b68bc98792d2cf5b (1,158)

a3fa0d15dd83b910295d0b17f9d341e737eddcb8d9b8081758140584c710406e (1,074)

Twitter Posts (President Scored Anon)

Shape: 27,304 rows × 48 columns

Null counts: inReplyToId (3,270), quoteId (24,017)

Unique values: id (27,304), url (27,304), source (14)

Top 5 sources by count:

Twitter Web App (14,930)

Twitter for iPhone (8,494)

Sprout Social (2,933)

Twitter Media Studio (499)

Twitter for iPad (266)

Interesting Facts

Ad Reach Extremes: Some Facebook ads reached the maximum reported audience size of 1,000,001 and achieved up to 1,000,000 impressions, with the largest single‐ad spend of $474,999.

Page Concentration: Although 4,475 unique pages ran ads, the top page accounted for over 22% (55,503) of all ad entries.

Complete Numeric Coverage: The Facebook Ads dataset had zero nulls across all key numeric fields, ensuring a fully populated numeric profile.

Post Engagement Peak: The most‐liked Facebook post garnered 351,979 likes, and video views peaked at over 4.4 million for a single post.

Underperformance Indicator: Facebook Posts’ Overperforming Score ranged from –198.75 to 246.78, with a median of –2.74, suggesting many posts underperformed relative to expectations.

Viral Tweets: The highest tweet viewCount hit 333 million, far above the mean of 507,085, highlighting occasional viral reach.

Platform Usage Split: Over 54% of tweets originated from the Twitter Web App, with the remainder spread across mobile and third‐party tools.

Rapid Data Processing: Polars implementations processed these large datasets approximately 20–30% faster than Pandas, while pure‑Python solutions, despite their simplicity, ran about 2–3× slower on the full files.
