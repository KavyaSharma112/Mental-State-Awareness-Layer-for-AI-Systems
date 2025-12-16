import pandas as pd
import re
import nltk
import emoji
from nltk.corpus import stopwords
from better_profanity import profanity

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

input_path = "data/raw/twitter_raw_data.csv"

df = pd.read_csv(input_path)

print('Dataset loaded successfully!')
print("Shape : ", df.shape)
print('\nColumns:')
print(df.columns.tolist())

print("\nSample rows:")
print(df.head(3))

print(df.isna().any())

df = df[['tweet_id', 'hashtags', 'text', 'platform']]
print('\nColumns after selection: ')
print(df.columns.tolist())

# Detecting and removing Explicit Content
profanity.load_censor_words()
CUSTOM_SEXUAL_WORDS = [
    "porn", "porno", "nude", "rape",
    "blowjob", "handjob", "cum"
]
profanity.add_censor_words(CUSTOM_SEXUAL_WORDS)

def remove_explicit_content(text):
    return profanity.contains_profanity(text)

df["expicit_content"]=df["text"].apply(remove_explicit_content)
df = df[df["expicit_content"] == False].reset_index(drop=True)



def clean_text(text):
    if pd.isna(text):
        return ""
    
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

def clean_hashtags(tags):
    if pd.isna(tags):
        return ""
    
    tags = tags.lower()
    tags = re.sub(r'#', '', tags)
    tags = re.sub(r'[^a-z\s]', '', tags)
    tags = re.sub(r'\s+', ' ', tags).strip()

    return tags



df['text_clean'] = df['text'].apply(clean_text)
df['hashtags_clean'] = df['hashtags'].apply(clean_hashtags)


OUTPUT_PATH = "data/processed/twitter_cleaned.csv"
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nCleaned data saved to: {OUTPUT_PATH}")


print('\n Sample cleaned data:')
print(df[['text', 'text_clean', 'hashtags','hashtags_clean']].head(5))