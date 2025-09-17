import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download sentiment lexicon if not already
nltk.download('vader_lexicon')

# Sample dataset
data = {
    'RegNo': ['21CS001','21CS002','21CS003','21CS004','21CS005',
              '21CS006','21CS007','21CS008','21CS009','21CS010'],
    'CourseReview': [
        "The course was well structured and engaging.",
        "Lectures were dull and lacked clarity.",
        "Assignments were challenging but rewarding.",
        "I struggled to follow the topics.",
        "Excellent teaching and great examples.",
        "Too much theory, not enough practical work.",
        "Loved the interactive sessions.",
        "The pace was too fast and confusing.",
        "Very informative and well delivered.",
        "Poor coordination and late feedback."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()
df['Sentiment'] = df['CourseReview'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Categorize into Positive / Negative
df['Label'] = df['Sentiment'].apply(lambda x: 'Positive' if x >= 0 else 'Negative')

print(df[['RegNo','CourseReview','Label']])
print("\nPositive count:", (df['Label']=='Positive').sum())
print("Negative count:", (df['Label']=='Negative').sum())
