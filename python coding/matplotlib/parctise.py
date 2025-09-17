import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create fake Delhi pollution data for 36 months
months = np.arange(1, 37)
pollution = np.random.normal(120, 30, size=36)

# Make some months outliers
pollution[4] = 200   # May outlier at month 5
pollution[10] = 210  # Outlier at month 11
pollution[20] = 180  # Outlier at month 21

# Find outliers: anything > mean + 2*std
threshold = pollution.mean() + 2 * pollution.std()
outlier_months = months[pollution > threshold]
outlier_rates = pollution[pollution > threshold]

# Find month with highest pollution
max_month = months[np.argmax(pollution)]
max_pollution = pollution.max()

# Draw the graph
plt.scatter(months, pollution, color='blue')
plt.scatter(outlier_months, outlier_rates, color='red', s=100, label="Outliers")
plt.scatter(max_month, max_pollution, color='green', s=120, label="Highest Pollution")
plt.xlabel("Month")
plt.ylabel("Pollution Rate")
plt.title("Delhi Pollution Rate Over 3 Years")
plt.legend()
plt.show()
