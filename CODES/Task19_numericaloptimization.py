import numpy as np
from scipy.optimize import minimize

# Cost function
def cost(z):

    x, y = z

    return 12*x + 18*y

# Capacity constraint
def capacity_constraint(z):

    x, y = z

    return 100*x + 170*y - 1000

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

bounds = [
    (0, None),
    (0, None)
]

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)

print("Type A allocation:", x)
print("Type B allocation:", y)

print(
    "Total capacity:",
    100*x + 170*y
)

print(
    "Minimum planning cost:",
    solution.fun
)

# Check whole-server combinations
best_integer = None

for a in range(0, 20):

    for b in range(0, 20):

        capacity = 100*a + 170*b

        if capacity >= 1000:

            total_cost = 12*a + 18*b

            if (
                best_integer is None
                or total_cost < best_integer[0]
            ):

                best_integer = (
                    total_cost,
                    a,
                    b,
                    capacity
                )

print("Best integer solution:", best_integer)