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
- Collection of real-world Twitter posts related to mental well-being and emotional states
- Implementation of a text preprocessing pipeline:
  - Cleaning tweet text (URLs, mentions, emojis, punctuation, stopwords)
  - Preserving and cleaning hashtags as a separate semantic feature
- Creation of an intermediate cleaned dataset for reproducibility
- Manual human annotation of tweets with emotion and distress labels:
  - Defined a 5-class emotion taxonomy (Neutral, Joy, Sadness, Anxiety/Fear, Distress)
  - Annotated each tweet with a single dominant emotion label
  - Generated a supervised learning–ready labeled dataset

## Next Steps
- Validate labeled dataset (label distribution, edge-case review)
- Exploratory Data Analysis (EDA) on emotion class balance and text patterns
- Train baseline emotion classification models (e.g., Logistic Regression, SVM)
- Compare model predictions against human-labeled ground truth
- Experiment with transformer-based models (BERT) for improved performance
- Integrate emotion detection into a safety-aware NLP pipeline

## Annotation Notes
- Labels were assigned manually to reflect the dominant emotional state of each tweet
- Ambiguous or contextual tweets were conservatively labeled as Neutral
- Distress labels were reserved for explicit emotional numbness, exhaustion, or vulnerability


