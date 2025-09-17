import matplotlib.pyplot as plt
import numpy as np
# Sample Data (Temperature in °C, Rainfall in mm)
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 29, 33] # Example temperature
#values
rainfall = [12, 8, 15, 10, 5] # Example rainfall
#values
plt.pie(rainfall, labels=days, autopct="%1.1f%%",startangle=90,colors=["skyblue", "lightgreen", "pink", "gold","violet"])
plt.title("Rainfall Contribution over 5 Days")
plt.show()