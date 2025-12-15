# Mental Well-Being Signal Detection from Social Media

## Overview
This project aims to detect implicit mental well-being signals from public social media text using Natural Language Processing (NLP).  
The focus is on identifying subtle linguistic patterns rather than explicit mental health keywords.

## Data Sources
- Twitter (public English tweets)
- Reddit (public posts – planned)

## Ethical Considerations
- Only publicly available data is used
- No user identifiers are stored
- Analysis is performed at an aggregate level
- This project does NOT attempt diagnosis

## Current Stage
- Project setup and repository structure finalized
- Twitter API integration for data collection
- Collection of real-world Twitter posts related to mental well-being
- Implementation of a text preprocessing pipeline:
  - Cleaning tweet text (URLs, mentions, emojis, punctuation, stopwords)
  - Preserving and cleaning hashtags as a separate semantic feature
- Creation of an intermediate cleaned dataset for reproducibility

## Next Steps
- Emotion labeling using a lexicon-based approach (NRC Emotion Lexicon)
- Emoji-based emotion scoring to capture sarcasm and tone
- Exploratory data analysis (EDA) on emotion distribution
- Generation of a final `cleaned_dataset.csv` for machine learning models

