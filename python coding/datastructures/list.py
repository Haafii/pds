# -------------------------------------------
# 1. First 10 Square Numbers
# -------------------------------------------
print("\n1. First 10 Square Numbers")

# Using a loop
squares = []
for i in range(1, 11):
    squares.append(i**2)
print("Loop:", squares)

# Using list comprehension
squares = [i**2 for i in range(1, 11)]
print("List Comprehension:", squares)


# -------------------------------------------
# 2. Remove Duplicates (Preserve Order)
# -------------------------------------------
print("\n2. Remove Duplicates (Preserve Order)")

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))


# -------------------------------------------
# 3. Slicing Logic
# -------------------------------------------
print("\n3. Slicing Logic")

my_list = [1, 2, 3, 4, 5]
print("Reversed:", my_list[::-1])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Every 3rd element:", my_list[::3])


# -------------------------------------------
# 4. Matrix Representation
# -------------------------------------------
print("\n4. Matrix Representation")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal = [matrix[i][i] for i in range(3)]
print("Diagonal:", diagonal)


# -------------------------------------------
# 5. Sorting Challenge
# -------------------------------------------
print("\n5. Sorting Challenge")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 80]
paired = list(zip(names, scores))
paired.sort(key=lambda x: x[1], reverse=True)
for name, score in paired:
    print(name, score)


# -------------------------------------------
# 6. Unpacking
# -------------------------------------------
print("\n6. Unpacking")

data = [10, 20, 30, 40]
first, *rest = data
print("First:", first)
print("Rest:", rest)


# -------------------------------------------
# 7. Flatten a Nested List
# -------------------------------------------
print("\n7. Flatten a Nested List")

nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]
print("Flattened:", flat)


# -------------------------------------------
# 8. List vs Set
# -------------------------------------------
print("\n8. List vs Set")

my_list = [1, 2, 2, 3]
unique_set = set(my_list)
print("List:", my_list)
print("Set:", unique_set)


# -------------------------------------------
# 9. Memory Management
# -------------------------------------------
print("\n9. Memory Management")

list1 = [1, 2, 3]
list2 = list1          # Same memory reference
list3 = list1.copy()   # New memory reference

list2.append(4)
print("list1:", list1)  # Affected
print("list3:", list3)  # Unaffected


# -------------------------------------------
# 10. AI Applications – Tokenization & Stopword Removal
# -------------------------------------------
print("\n10. AI Applications – Tokenization & Stopword Removal")

sentence = "This is a simple example for NLP"
stopwords = {"is", "a", "for"}

# Tokenization
tokens = sentence.lower().split()
# Remove stopwords
filtered = [word for word in tokens if word not in stopwords]
print("Filtered:", filtered)
