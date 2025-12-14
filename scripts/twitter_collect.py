import os
import tweepy
import pandas as pd
from datetime import datetime

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

if BEARER_TOKEN is None:
    raise ValueError("Bearer token not found. Set TWITTER_BEARER_TOKEN.")

client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

query = (
    '"mentally exhausted" OR "everything feels too much" OR '
    '"don’t feel like talking" OR "feel empty" OR '
    '"nothing feels right" OR "I feel off" OR '
    '"can’t think straight" OR "brain feels foggy" OR '
    '"feel overwhelmed" OR "too much going on" OR '
    '"feel numb" OR "lost interest in everything" OR '
    '"hard to care anymore" OR "barely coping" '
    'lang:en -is:retweet -has:links'
)

try:
    response = client.search_recent_tweets(
        query=query,
        max_results=50,
        tweet_fields=["created_at", "lang", "entities"],
        user_fields=["location"],
        expansions=["author_id"]
    )
except Exception as e:
    print("Twitter API request failed.")
    print("Reason:", e)
    print("This is likely due to rate limiting or connection reset.")
    exit()


records = []

if response.data and "users" in response.includes:
    user_lookup = {user.id: user for user in response.includes["users"]}

    for tweet in response.data:
        user = user_lookup.get(tweet.author_id)

        hashtags = []
        if tweet.entities and "hashtags" in tweet.entities:
            hashtags = [tag["tag"] for tag in tweet.entities["hashtags"]]

        records.append({
            "platform": "twitter",
            "tweet_id": tweet.id,
            "text": tweet.text,
            "hashtags": hashtags,
            "created_at": tweet.created_at,
            "language": tweet.lang,
            "user_location": user.location if user else None,
            "collected_at": datetime.utcnow()
        })



df = pd.DataFrame(records)
output_path = "data/raw/twitter_raw_data.csv"
df.to_csv(output_path, index=False)

print(f"Collected {len(df)} tweets and data saved to {output_path}.")