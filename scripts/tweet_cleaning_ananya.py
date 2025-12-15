import pandas as pd
import re

#Ananya
# Remove emojis
def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

# Remove URLs
def remove_links(text):
    return re.sub(r'http\S+|www\S+|https\S+', '', text)

# Clean text column
def clean_text(text):
    if pd.isna(text):
        return text
    text = str(text)
    text = remove_links(text)
    text = remove_emojis(text)
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = text.strip()
    return text

# Load CSV
input_file = "data/raw/twitter_raw_data.csv"     # change filename if needed
output_file = "data/processed/twitter_cleaned_data(ananya).csv"

df = pd.read_csv(input_file)

# Specify the column(s) containing text
text_columns = ["text"]   # change if your column name is different

# Apply cleaning
for col in text_columns:
    df[col] = df[col].apply(clean_text)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Optional: remove rows where text is empty
df = df[df["text"].str.strip() != ""]

# Save cleaned CSV
df.to_csv(output_file, index=False)
print("Data cleaning completed!")
print(f"Cleaned file saved as: {output_file}")
