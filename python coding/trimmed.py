import pandas as pd

# Load your dataset
df = pd.read_csv('your_dataset.csv')  # or pd.read_excel(), etc.

# Trim to first 100 rows
df_trimmed = df.head(100)

# Optionally, save it
df_trimmed.to_csv('trimmed_dataset.csv', index=False)