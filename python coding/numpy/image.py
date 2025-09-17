import numpy as np

# Create 8x8 binary image (random 0s and 1s)
image = np.random.randint(0, 2, (8, 8))
print("8x8 Binary Image:\n", image)

# Split into 4x4 segments
seg1 = image[0:4, 0:4]   # Top-left
seg2 = image[0:4, 4:8]   # Top-right
seg3 = image[4:8, 0:4]   # Bottom-left
seg4 = image[4:8, 4:8]   # Bottom-right

# Calculate means
mean1 = seg1.mean()
mean2 = seg2.mean()
mean3 = seg3.mean()
mean4 = seg4.mean()

# Print results
print("\nMean of Top-left 4x4:", mean1)
print("Mean of Top-right 4x4:", mean2)
print("Mean of Bottom-left 4x4:", mean3)
print("Mean of Bottom-right 4x4:", mean4)

# Find brightest segment (highest mean)
means = [mean1, mean2, mean3, mean4]
brightest_index = np.argmax(means)
segments = ["Top-left", "Top-right", "Bottom-left", "Bottom-right"]

print("\nBrightest Segment:", segments[brightest_index])
