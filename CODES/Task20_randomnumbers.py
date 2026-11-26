import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0

N = 100000

# Generate random demand scenarios
demand = rng.normal(
    mean_demand,
    std_demand,
    N
)

# Identify overloaded cases
overloaded = demand > capacity

overload_probability = overloaded.mean()

print(
    "Estimated overload probability:",
    f"{overload_probability:.4%}"
)

print(
    "Number of overload cases:",
    overloaded.sum(),
    "out of",
    N
)

# Running probability
running_probability = (
    np.cumsum(overloaded)
    / np.arange(1, N + 1)
)

indices = np.unique(
    np.logspace(
        1,
        np.log10(N),
        200
    ).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")

plt.title(
    "Monte Carlo estimate of server-overload risk"
)

plt.grid(True)
plt.show()