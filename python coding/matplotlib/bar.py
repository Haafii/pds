import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
# Sample Data (Temperature in °C, Rainfall in mm)
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 29, 33] # Example temperaturevalues

plt.bar(days, temperature, color=["orange", "blue", "green","red", "purple"])
plt.title("Daily Temperatures")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()