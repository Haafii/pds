import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
# Sample Data (Temperature in °C, Rainfall in mm)
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 29, 33] # Example temperaturevalues
rainfall = [12, 8, 15, 10, 5] # Example rainfallvalues
day_indices = [2, 4] # Wed & Fri indices
temps_compare = [temperature[2], temperature[4]]
plt.scatter(["Wednesday", "Friday"], temps_compare,color=["red", "green"], s=[100, 150])
plt.title("Temperature Comparison: Wednesday vs Friday")
plt.ylabel("Temperature (°C)")
plt.show()