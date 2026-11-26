import numpy as np
from scipy.optimize import root_scalar

# Heat balance function
def f(T):
    return T - 25 - 10 * np.exp(-T / 20)

# Bisection method
bisection = root_scalar(
    f,
    bracket=[20, 40],
    method="bisect"
)

print("Bisection root:", bisection.root)

# Fixed-point iteration
x = 30

for i in range(100):
    new_x = 25 + 10 * np.exp(-x / 20)

    if abs(new_x - x) < 1e-8:
        break

    x = new_x

print("Fixed-point root:", x)