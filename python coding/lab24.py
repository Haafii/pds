# Step 1: Patient data (name, age, list of temperature readings)
patients = [
    ("Alice", 30, [98.6, 99.1, 100.2]),
    ("Bob", 45, [97.9, 98.4, 98.6]),
    ("Charlie", 50, [99.5, 100.1, 100.3]),
    ("Daisy", 25, [98.8, 99.0, 98.7]),
    ("Ethan", 60, [99.9, 100.4, 101.2])
]

# Step 2: Identify patients with average temp > 99°F
high_temp_patients = []

for name, age, temps in patients:
    avg_temp = sum(temps) / len(temps)
    if avg_temp > 99:
        high_temp_patients.append((name, round(avg_temp, 2)))


print("Patients with fever (avg temp > 99°F):")
for patient in high_temp_patients:
    print(patient)
