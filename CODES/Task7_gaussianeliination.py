import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [3, 1, 1],
    [1, 4, 2],
    [2, 1, 5]
], dtype=float)

# Factorize matrix
lu, piv = lu_factor(A)

# Different right-hand-side vectors
B1 = np.array([15, 10, 10], dtype=float)
B2 = np.array([18, 12, 15], dtype=float)

# Solve both systems
x1 = lu_solve((lu, piv), B1)
x2 = lu_solve((lu, piv), B2)

print("Solution 1:", x1)
print("Solution 2:", x2)

print("Residual 1:", np.linalg.norm(A @ x1 - B1))
print("Residual 2:", np.linalg.norm(A @ x2 - B2))