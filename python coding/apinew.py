import requests
import datetime

# Your Windy API key
API_KEY = "3fUU0naF17ttzgsactxQTYpAv0QRwdou"

# Location: Chennai, India
lat = 13.0827
lon = 80.2707

# Windy Point Forecast API endpoint
url = "https://api.windy.com/api/point-forecast/v2"

# Headers with API key
headers = {
    "Content-Type": "application/json",
    "x-windy-key": API_KEY
}

# Payload with required parameters
payload = {
    "lat": lat,
    "lon": lon,
    "model": "gfs",  # Forecast model (GFS = Global Forecast System)
    "parameters": ["temp", "wind", "precip"],  # Request temperature, wind, precipitation
    "levels": ["surface"],  # Surface level forecast
    "key": API_KEY
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    timestamps = data["ts"]  # forecast timestamps
    temp_values = data["temp-surface"]  # surface temperature
    wind_u_values = data["wind_u-surface"]  # wind east-west component
    wind_v_values = data["wind_v-surface"]  # wind north-south component
    rain_values = data["past3hprecip-surface"]  # precipitation
    
    print("Weather Forecast for Chennai:")
    print("-" * 60)
    
    for i in range(len(timestamps)):
        # Convert timestamp from ms → human-readable UTC
        time = datetime.datetime.utcfromtimestamp(timestamps[i] / 1000)
        
        # Convert temperature from Kelvin → Celsius
        temp_celsius = temp_values[i] - 273.15
        
        # Print formatted forecast
        print(f"{time} | Temp: {temp_celsius:.2f}°C | "
              f"Wind u: {wind_u_values[i]:.2f} m/s | "
              f"Wind v: {wind_v_values[i]:.2f} m/s | "
              f"Rain: {rain_values[i]} mm")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
