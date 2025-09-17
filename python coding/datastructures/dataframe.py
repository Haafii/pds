import pandas as pd
import numpy as np


df = pd.DataFrame({
'Name': ['Aarav', 'Diya', 'Kabir', 'Riya', 'Raj'],
'Score': [85, 92, 78, 88, 75],
'Sales': [5000, 6000, 4000, 5500, 4500],
'Region': ['North', 'South', 'East', 'West', 'South']
})
df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
df['Grade'] = np.where(df['Score'] >= 90, 'A', 'B')
df['Name'] = df['Name'].replace('Aarav', 'Aarav Gupta')
df.groupby('Region').agg({'Score':['mean','sum']})