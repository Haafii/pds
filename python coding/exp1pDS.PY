import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Step 2: Select only Name and Age columns
name_age_df = df[['Name', 'Age']]
print("\nSelected Name and Age columns:\n", name_age_df)

# Step 3: Filter rows where Age is greater than 25
age_filtered_df = df[df['Age'] > 25]
print("\nFiltered rows (Age > 25):\n", age_filtered_df)

# Step 4: Add new column 'Country' with default value 'USA'
df['Country'] = 'USA'
print("\nDataFrame after adding 'Country' column:\n", df)

# Step 5: Sort the DataFrame by Age in descending order
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):\n", sorted_df)

# Step 6: Calculate the average age
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)
