size = 5  # You can change this to any size

for row in range(size):
    for col in range(size):
        # Print star if we're on the border
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line