import pandas as pd

df = pd.read_csv("data/labeled/twitter_emotion_labeled_duplicatesRemoved.csv")
print(df.head(3))

# Label mapping (numeric → human-readable)
label_map = {
    0: 'neutral',
    1: 'joy',
    2: 'sadness',
    3: 'anxiety/fear',
    4: 'distress'
}

# Label distribution
df['emotion_name'] = df['emotion_label'].map(label_map)
label_counts = df['emotion_name'].value_counts()
print("\nLabel distribution: ")
print(label_counts)
print("\nLabel distribtuion (percentage): ")
print((label_counts / len(df)) * 100)

# Basic Text insights
df['tweet_length']=df['text_clean'].apply(lambda x: len(str(x).split()))
print("\nOverall Average Tweet Length : ")
print(df['tweet_length'].mean())
avg_length_per_emotion = df.groupby('emotion_label')['tweet_length'].mean()
print("\nAverage Tweet length per emotion : ")
print(avg_length_per_emotion)

from collections import Counter

def most_common_words(texts, n=10):
    all_words = ' '.join(texts).split()
    return Counter(all_words).most_common(n)

for emotion in df['emotion_name'].unique():
    emotion_texts = df[df['emotion_name'] == emotion]['text_clean']
    common_words = most_common_words(emotion_texts, n=10)

    print(f"\nMost common words for {emotion} :")
    print(common_words)