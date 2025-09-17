import numpy as np
# Create 8x8 binary image
image = np.random.randint(0, 2, (8, 8))
print("8x8 Binary Image:\n", image)
# Divide into 4x4 segments
seg1 = image[0:4, 0:4]
seg2 = image[0:4, 4:8]
seg3 = image[4:8, 0:4]
seg4 = image[4:8, 4:8]
# Compute mean of each segment
print("Mean of Top-left 4x4:", seg1.mean())
print("Mean of Top-right 4x4:", seg2.mean())
print("Mean of Bottom-left 4x4:", seg3.mean())
print("Mean of Bottom-right 4x4:", seg4.mean())