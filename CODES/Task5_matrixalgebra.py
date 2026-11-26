import numpy as np

# Coordinates of a square
points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

# Rotation angle
angle = np.radians(45)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Scaling matrix
scaling = np.array([
    [2, 0],
    [0, 1.5]
])

# Apply transformations
transformed = points @ rotation.T @ scaling.T

print("Original coordinates:")
print(points)

print("Transformed coordinates:")
print(transformed)

print("Determinant:")
print(np.linalg.det(rotation))