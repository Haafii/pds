import numpy as np

# Create a 20x20 binary image (1 = urban, 0 = natural)
np.random.seed(42)  # for reproducibility
image = np.random.randint(0, 2, (20, 20))
print("20x20 Binary Image:\n", image)

# Segment size
segment_size = 4
dense_threshold = 0.8  # 80%

dense_segments = 0

# Iterate over 4x4 segments
for i in range(0, 20, segment_size):
    for j in range(0, 20, segment_size):
        segment = image[i:i+segment_size, j:j+segment_size]
        urban_ratio = segment.mean()  # fraction of urban pixels
        if urban_ratio >= dense_threshold:
            dense_segments += 1

# Total urban and natural areas
total_urban = image.sum()
total_natural = image.size - total_urban

# Urban pixels in boundary
boundary_pixels = np.concatenate([
    image[0, :],        # top row
    image[-1, :],       # bottom row
    image[1:-1, 0],     # left column without corners
    image[1:-1, -1]     # right column without corners
])
boundary_urban = boundary_pixels.sum()

print("\nTotal urban pixels:", total_urban)
print("Total natural pixels:", total_natural)
print("Number of 4x4 dense urban segments (>=80%):", dense_segments)
print("Number of urban pixels in boundary region:", boundary_urban)
