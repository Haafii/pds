import requests
import datetime

API_KEY = "QojSQxL1Kb8YN1PRuv1Z92ufHfosxiCh"

lat = 13.0827
lon = 80.2707

url = "https://api.windy.com/api/point-forecast/v2"
headers = {
    "Content-Type": "application/json",
    "x-windy-key": API_KEY
}
payload = {
    "lat": lat,
    "lon": lon,
    "model": "gfs",  # Global Forecast System
    "parameters": ["temp", "wind", "precip"], 
    "levels": ["surface"],
    "key": API_KEY
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    timestamps = data["ts"]  # List of timestamps
    temp_values = data["temp-surface"]
    wind_u_values = data["wind_u-surface"]
    wind_v_values = data["wind_v-surface"]
    rain_values = data["past3hprecip-surface"]

    print("Weather Forecast:")
    for i in range(len(timestamps)):
        time = datetime.datetime.utcfromtimestamp(timestamps[i] / 1000)
        temp_celsius = temp_values[i] - 273.15  # Convert Kelvin to Celsius
        print(
            f"{time} | Temp: {temp_celsius:.2f}°C | "
            f"Wind u: {wind_u_values[i]:.2f} m/s | "
            f"Wind v: {wind_v_values[i]:.2f} m/s | "
            f"Rain: {rain_values[i]} mm"
        )
else:
    print(f"Error: {response.status_code}")
    print(response.text)
