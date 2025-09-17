
students = (("Alice", 85), ("Bob", 90), ("Charlie", 80))
sorted_students = tuple(sorted(students, key=lambda x: x[1],
reverse=True))
print(sorted_students)
# Output: (('Bob', 90), ('Alice', 85), ('Charlie', 80))

products = [("Laptop", 45000), ("Mouse", 300), ("Keyboard",
700)]
cheap_products = [p for p in products if p[1] < 500]
print(cheap_products)
# Output: [('Mouse', 300)]

# Answer:
data = (("name", "Sasikala"), ("year", 2025), ("active",
True))
data_dict = dict(data)
print(data_dict)
# Output: {'name': 'Sasikala', 'year': 2025, 'active': True}

nested = (1, (2, 3, (4, 5, (6, 7))))
# Answer:
nested = (1, (2, 3, (4, 5, (6, 7))))
value = nested[1][2][2][1]
print(value)
# Output: 7

# Answer:
def pack_into_tuple(*args):
    return args
print(pack_into_tuple("AI", "Python", 2025))
# Output: ('AI', 'Python', 2025)

# Answer:
t1 = (1, 2, 3)
t2 = (3, 2, 1)
xor_result = tuple(a ^ b for a, b in zip(t1, t2))
print(xor_result)
# Output: (2, 0, 2)

# Answer:
nums = (1, 2, 2, 3, 3, 3)
freq = {num: nums.count(num) for num in set(nums)}
print(freq)
# Output: {1: 1, 2: 2, 3: 3}
