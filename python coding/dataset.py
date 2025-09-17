import random
import datetime
import pandas as pd

def generate_watch_dataset(num_rows=20, start_time=None, interval_seconds=60):
    if start_time is None:
        start_time = datetime.datetime.now()
    rows = []
    for i in range(num_rows):
        ts = start_time + datetime.timedelta(seconds=i*interval_seconds)
        temp = round(random.uniform(20, 35), 1)
        temp_max = temp + round(random.uniform(0, 2), 1)
        temp_min = temp - round(random.uniform(0, 2), 1)
        humidity = round(random.uniform(30, 90), 1)
        dew_point = round(temp - (100 - humidity) / 5, 1)
        heat_index = round(temp + 0.1 * humidity, 1)
        pressure = round(random.uniform(1000, 1025), 1)
        wind_speed = round(random.uniform(0, 20), 1)
        conditions = random.choice(["Clear", "Cloudy", "Rain", "Snow", "Fog"])
        rows.append({
            "timestamp": ts.isoformat(),
            "temperature_C": temp,
            "temp_max_C": temp_max,
            "temp_min_C": temp_min,
            "humidity_%": humidity,
            "dew_point_C": dew_point,
            "heat_index_C": heat_index,
            "pressure_hPa": pressure,
            "wind_speed_kmh": wind_speed,
            "conditions": conditions
        })
    return pd.DataFrame(rows)

# Generate and save
df = generate_watch_dataset()
df.to_csv("watch_temperature_dataset.csv", index=False)