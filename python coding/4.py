#Count how many times each digit (0-9) appears in a given integer using a loop and dictionary.
number = (input("enter the number"))
dictionary = {}
for i in range(0, 10):
    dictionary[str(i)] = 0

for i in number:
    dictionary[i] = dictionary[i]+1
print(dictionary)