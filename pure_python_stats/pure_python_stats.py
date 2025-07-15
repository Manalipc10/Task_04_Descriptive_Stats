#!/usr/bin/env python
from fb_ads_pure_python import analyze_fb_ads
from tw_posts_pure_python import analyze_tw_posts
from fb_posts_pure_python import analyze_fb_posts
CSV_FILE = [
    r"../data/2024_fb_ads_president_scored_anon.csv",
    r"..\\data\\2024_fb_posts_president_scored_anon.csv",
    r"../data/2024_tw_posts_president_scored_anon.csv"
]

def main():

    print("FB Ads President Scored Anon dataset")

    analyze_fb_ads(CSV_FILE[0], top_n_groups=10)

    print("FB Posts President Scored Anon dataset")
    analyze_fb_posts(CSV_FILE[1], top_n_groups=10)
    print("TW Posts President Scored Anon dataset")

    analyze_tw_posts(CSV_FILE[2], top_n_groups=10)


if __name__ == "__main__":
    main()