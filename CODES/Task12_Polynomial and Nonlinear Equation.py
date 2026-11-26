import numpy as np
from scipy.optimize import root

def equations(z):
    x, y = z

    return [
        x**2 + y**2 - 4,
        y - x**2 + 1
    ]

# Initial guess
initial = [1, 1]

solution = root(equations, initial)

print("Solver success:", solution.success)
print("X value:", solution.x[0])
print("Y value:", solution.x[1])
print("Residuals:", equations(solution.x))