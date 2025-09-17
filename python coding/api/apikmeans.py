import requests
import datetime
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# -----------------------------
# API Setup
# -----------------------------
API_KEY = "3fUU0naF17ttzgsactxQTYpAv0QRwdou"  # Replace with your Windy API key
url = "https://api.windy.com/api/point-forecast/v2"

headers = {
    "Content-Type": "application/json",
    "x-windy-key": API_KEY
}

# Define grid of locations (example around Chennai)
lats = [13 + 0.2 * i for i in range(4)]
lons = [80 + 0.2 * j for j in range(4)]
grid_points = [(lat, lon) for lat in lats for lon in lons]

weather_data = []

# -----------------------------
# Fetch Weather Data
# -----------------------------
for lat, lon in grid_points:
    payload = {
        "lat": lat,
        "lon": lon,
        "model": "gfs",
        "parameters": ["temp", "wind", "precip"],
        "levels": ["surface"],
        "key": API_KEY
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        timestamps = data.get("ts", [])
        temp_values = data.get("temp-surface", [])
        wind_u_values = data.get("wind_u-surface", [])
        wind_v_values = data.get("wind_v-surface", [])
        rain_values = data.get("past3hprecip-surface", [])

        if temp_values and wind_u_values and wind_v_values and rain_values:
            avg_temp = sum(temp_values) / len(temp_values) - 273.15
            avg_wind_u = sum(wind_u_values) / len(wind_u_values)
            avg_wind_v = sum(wind_v_values) / len(wind_v_values)
            avg_rain = sum(rain_values) / len(rain_values)

            weather_data.append([lat, lon, avg_temp, avg_wind_u, avg_wind_v, avg_rain])

    except requests.exceptions.RequestException as err:
        print(f"Request error for ({lat}, {lon}): {err}")
    except Exception as err:
        print(f"Error processing data for ({lat}, {lon}): {err}")

# -----------------------------
# DataFrame for Analysis
# -----------------------------
if weather_data:
    df_weather = pd.DataFrame(weather_data, columns=["lat", "lon", "temp", "wind_u", "wind_v", "rain"])
    print(df_weather.head())

    # -----------------------------
    # K-Means Clustering
    # -----------------------------
    X = df_weather[["temp", "wind_u", "wind_v", "rain"]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    distortions = []
    K = range(1, 6)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        distortions.append(kmeans.inertia_)

    # Elbow Method Plot
    plt.plot(K, distortions, "bx-")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method For Optimal K")
    plt.show()

    # -----------------------------
    # Fit KMeans with optimal K (example: k=3)
    # -----------------------------
    optimal_k = 3
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df_weather["Cluster"] = kmeans.fit_predict(X_scaled)

    print("\nWeather Zones Identified (using K-means):")
    print(df_weather[["lat", "lon", "Cluster"]])

    # Cluster Centroids (average weather conditions)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    centroids_df = pd.DataFrame(centroids, columns=["temp", "wind_u", "wind_v", "rain"])
    print("\nCluster Centroids (average weather for each zone):")
    print(centroids_df)

else:
    print("No weather data was retrieved. Cannot perform K-means analysis.")
