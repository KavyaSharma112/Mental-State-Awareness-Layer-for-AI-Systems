import pandas as pd

df = pd.read_csv("data/labeled/twitter_emotion_labeled.csv",
                 engine="python",
                 on_bad_lines='skip')
print('Before removing duplicates : ', len(df))
df_duplicatesRemoved = df.drop_duplicates(subset=['text_clean'], keep = 'first')
print('Before removing duplicates : ', len(df_duplicatesRemoved))

df_duplicatesRemoved.to_csv("data/labeled/twitter_emotion_labeled_duplicatesRemoved.csv", index=False)

print('Duplicates removed and new file saved successfully!')