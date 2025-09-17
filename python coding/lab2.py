import copy


employees = [("Alice", 4.2), ("Bob", 3.8), ("Charlie", 4.7), ("David", 4.0)]

copied_employees = copy.deepcopy(employees)

# Remove the employee with the lowest rating from the deep copy
lowest = min(copied_employees, key=lambda x: x[1])
copied_employees.remove(lowest)

#Count the number of employees in both lists
print("Original list count:", len(employees))
print("Copied list count:", len(copied_employees))

#Sort employees by rating (descending)
sorted_employees = sorted(employees, key=lambda x: x[1], reverse=True)
print("\nSorted Employees (Original List):")
for emp in sorted_employees:
    print(emp)

#Print employee name with the highest rating
highest = max(employees, key=lambda x: x[1])
print("\nHighest Rated Employee:", highest[0])

copied_employees.clear()


print("\nFinal Original List:", employees)
print("Final Copied List (After Clearing):", copied_employees)
