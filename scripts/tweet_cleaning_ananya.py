import pandas as pd
import re
import nltk
import emoji
from nltk.corpus import stopwords

# 1. NLTK SETUP

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# 2. LOAD DATA

input_path = "data/raw/twitter_raw_data(ananya).csv"
df = pd.read_csv(input_path)

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# 3. SELECT REQUIRED COLUMNS

df = df[['tweet_id', 'hashtags', 'text', 'platform']]

# 4. STRONG EMOJI REMOVAL

def remove_emojis_regex(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)

# 5. EXPLICIT / OFFENSIVE WORD LIST

explicit_words = {
    "fuck", "fucking", "porno", "handjob", "blowjob",
     "porn", "nude", "nudes", "slut", "cum", "rape"
}

def contains_explicit(text):
    words = set(text.split())
    return bool(words.intersection(explicit_words))

# 6. TEXT CLEANING FUNCTION

def clean_text(text):
    if pd.isna(text):
        return ""

    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove mentions
    text = re.sub(r'@\w+', '', text)

    # Remove hashtag symbol
    text = re.sub(r'#', '', text)

    # Remove emojis
    text = emoji.replace_emoji(text, replace='')
    text = remove_emojis_regex(text)

    # Remove non-alphabet characters
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

# 7. HASHTAG CLEANING

def clean_hashtags(tags):
    if pd.isna(tags):
        return ""

    tags = tags.lower()
    tags = re.sub(r'#', '', tags)
    tags = re.sub(r'[^a-z\s]', ' ', tags)
    tags = re.sub(r'\s+', ' ', tags).strip()

    return tags

# 8. APPLY CLEANING

df['text_clean'] = df['text'].apply(clean_text)
df['hashtags_clean'] = df['hashtags'].apply(clean_hashtags)

# 9. REMOVE EMPTY COMMENTS

df = df[df['text_clean'] != ""]

# 10. REMOVE EXPLICIT / OFFENSIVE COMMENTS

df = df[~df['text_clean'].apply(contains_explicit)]

# 11. REMOVE DUPLICATES (AFTER CLEANING)

df = df.drop_duplicates(subset=['text_clean'])

print("Shape after cleaning:", df.shape)

# 12. SAVE CLEANED DATA

output_path = "data/processed/twitter_cleaned(ananya).csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned data saved to: {output_path}")

# 13. SAMPLE OUTPUT

print("\nSample cleaned data:")
print(df[['text', 'text_clean', 'hashtags', 'hashtags_clean']].head(5))
