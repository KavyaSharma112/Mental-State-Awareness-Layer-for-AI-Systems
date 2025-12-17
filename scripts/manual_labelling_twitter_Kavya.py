import pandas as pd

# Paths
input_path = "data/processed/twitter_cleaned.csv"
output_path = "data/labeled/twitter_emotion_labeled.csv"

# Load cleaned data
df = pd.read_csv(input_path)

# Select only required columns
df_labeled = df[[
    "tweet_id",
    "text_clean",
    "hashtags_clean"
]].copy()

# Add empty emotion label column
df_labeled["emotion_label"] = ""

# Save labeled dataset
df_labeled.to_csv(output_path, index=False)

print("✅ Labeled dataset template created successfully!")
print(f"📁 Saved at: {output_path}")
