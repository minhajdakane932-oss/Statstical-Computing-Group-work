import numpy as np

# Coefficient matrix
A = np.array([
    [2, 1],
    [1, 3]
])

# Required resources
B = np.array([20, 72])

# Solve equations
solution = np.linalg.solve(A, B)

print("Solution:", solution)

# Verify the answer
print("Verification:", A @ solution)