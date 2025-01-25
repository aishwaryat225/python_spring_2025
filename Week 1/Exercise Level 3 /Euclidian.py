import math

# Coordinates
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance between (2, 3) and (10, 8) is: {distance:.2f}")
