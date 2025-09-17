import sqlite3
import pandas as pd

# Load Excel
df = pd.read_excel("SuperMarket Analysis.xlsx")

# Connect DB
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product TEXT,
    revenue REAL
)
''')

# Insert data
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO sales (date, product, revenue)
        VALUES (?, ?, ?)
    ''', (row['Date'], row['Product line'], row['Sales']))

# Commit + Close
conn.commit()
conn.close()

print("Database created and populated successfully")
