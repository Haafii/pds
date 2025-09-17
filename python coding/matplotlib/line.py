import matplotlib.pyplot as plt
import numpy as np
# Sample Data (Temperature in °C, Rainfall in mm)
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 29, 33] # Example temperature
#values
rainfall = [12, 8, 15, 10, 5] # Example rainfall
#values
# ------------------------------------------------------
# 1. Line Chart – Temperature Trend
# ------------------------------------------------------
plt.plot(days, temperature, marker='o', linestyle='-',
color='b', label="Temperature")
plt.title("Temperature Trend Over 5 Days")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.show()