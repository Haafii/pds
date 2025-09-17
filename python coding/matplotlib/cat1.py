import matplotlib.pyplot as plt
import pandas as pd

# Sample healthcare dataset
data = {
    'Facility': ['Hospitals','Clinics','Doctors','Nurses','Beds'],
    'Count': [250, 600, 1200, 3000, 15000]
}
df = pd.DataFrame(data)

# 1. Bar chart (comparison of facilities)
plt.bar(df['Facility'], df['Count'])
plt.title("Healthcare Facilities Comparison")
plt.xlabel("Facility")
plt.ylabel("Count")
plt.show()

# 2. Pie chart (distribution of resources)
plt.pie(df['Count'], labels=df['Facility'], autopct='%1.1f%%')
plt.title("Healthcare Resources Distribution")
plt.show()

# 3. Line chart (growth trend over years)
years = [2018,2019,2020,2021,2022,2023]
hospitals = [180,200,210,230,240,250]
plt.plot(years, hospitals, marker='o')
plt.title("Hospitals Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Hospitals")
plt.show()
