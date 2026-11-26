import numpy as np

A = np.array([
    [10, -1, 2, 0, 0],
    [-1, 11, -1, 3, 0],
    [2, -1, 10, -1, 0],
    [0, 3, -1, 8, -2],
    [0, 0, 0, -2, 5]
], dtype=float)

b = np.array([6, 25, -11, 15, 10], dtype=float)

# Initial estimate
x = np.zeros(5)

tolerance = 1e-5
max_iterations = 100

for iteration in range(max_iterations):

    old_x = x.copy()

    for i in range(5):
        x[i] = (
            b[i] - np.dot(A[i], x) + A[i, i] * x[i]
        ) / A[i, i]

    error = np.max(np.abs(x - old_x))

    if error < tolerance:
        break

print("Solution:", x)
print("Iterations:", iteration + 1)
print("Final error:", error)