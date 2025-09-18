import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch JSON data from Windy API
url = "https://api.windy.com/api/point-forecast/v2"

# Replace with your Windy API key
API_KEY = "YOUR_API_KEY"

# Example: Prague, Czech Republic (lat/lon)
payload = {
    "lat": 50.0755,
    "lon": 14.4378,
    "model": "gfs",                      # Forecast model: gfs, iconEu, etc.
    "parameters": ["temp", "wind", "rh"], # Temperature, wind speed, relative humidity
    "levels": ["surface"],                # At surface level
    "key": API_KEY
}

resp = requests.post(url, json=payload)

if resp.status_code == 200:
    data = resp.json()
    
    # Step 2: Convert to DataFrame
    df = pd.json_normalize(data, sep="_")
    
    # Step 3: Preprocessing
    print("Initial Data Info:")
    print(df.info())
    
    df = df.dropna(how="all")
    df = df.fillna(0)
    df = df.drop_duplicates()
    
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("category")
    
    # Step 4: Exploratory Data Analysis (Graphs)
    plt.figure(figsize=(10,6))
    df.hist(figsize=(12,8))
    plt.suptitle("Histograms of Numerical Columns")
    plt.show()
    
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
    
    num_cols = df.select_dtypes(include=["int64","float64"]).columns
    if len(num_cols) >= 2:
        plt.figure(figsize=(8,6))
        plt.scatter(df[num_cols[0]], df[num_cols[1]], alpha=0.6)
        plt.xlabel(num_cols[0])
        plt.ylabel(num_cols[1])
        plt.title("Scatter Plot")
        plt.show()
    
    cat_cols = df.select_dtypes(include="category").columns
    if len(cat_cols) > 0:
        plt.figure(figsize=(8,6))
        df[cat_cols[0]].value_counts().plot(kind="bar")
        plt.title(f"Distribution of {cat_cols[0]}")
        plt.show()
    
    # Step 5: Save processed data
    df.to_excel("windy_output.xlsx", index=False)
    print("Processed DataFrame saved to windy_output.xlsx")
    
else:
    print("Failed to fetch data. Status code:", resp.status_code, resp.text)