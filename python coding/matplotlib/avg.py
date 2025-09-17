import matplotlib.pyplot as plt
import numpy as np
# Sample Data (Temperature in °C, Rainfall in mm)
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 29, 33] # Example temperature
#values
rainfall = [12, 8, 15, 10, 5] # Example rainfall
#values
avg_temp = np.mean(temperature)
print(f"Average Temperature over 5 days: {avg_temp:.2f}°C")
# Annotating the average on line chart
plt.plot(days, temperature, marker='o', linestyle='-',color='b')
plt.axhline(y=avg_temp, color='r', linestyle='--',label=f"Avg Temp: {avg_temp:.2f}°C")
plt.title("Temperature Trend with Average Line")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()