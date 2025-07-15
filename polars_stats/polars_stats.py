#!/usr/bin/env python
import polars as pl
from fb_ads_polars import fb_ads_polars
from fb_posts_polars import fb_posts_polars
from tw_posts_polars import tw_posts_polars
CSV_FILE = [
    r"../data/2024_fb_ads_president_scored_anon.csv",
    r"..\\data\\2024_fb_posts_president_scored_anon.csv",
    r"../data/2024_tw_posts_president_scored_anon.csv"
]

print("FB Ads President Scored Anon dataset")
fb_ads_polars(CSV_FILE[0])

print("FB Posts President Scored Anon dataset")

fb_posts_polars(CSV_FILE[1])

print("TW Posts President Scored Anon dataset")
tw_posts_polars(CSV_FILE[2])