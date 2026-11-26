import numpy as np

# Network adjacency matrix
A = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
], dtype=float)

# Calculate eigenvalues and eigenvectors
values, vectors = np.linalg.eig(A)

# Find dominant eigenvector
index = np.argmax(values.real)

importance = np.abs(vectors[:, index].real)

# Normalize scores
importance = importance / importance.sum()

print("Eigenvalues:", values)
print("Importance scores:", importance)