import numpy as np
from scipy.integrate import simpson

# Power readings in kW
time_hours = np.array(
    [0, 2, 4, 6, 8, 10, 12],
    dtype=float
)

power_kw = np.array([
    0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9
])

# Trapezoidal rule
energy_trapezoid = np.trapezoid(
    power_kw,
    time_hours
)

# Simpson's rule
energy_simpson = simpson(
    power_kw,
    x=time_hours
)

print(
    "Energy using trapezoidal rule:",
    energy_trapezoid,
    "kWh"
)

print(
    "Energy using Simpson's rule:",
    energy_simpson,
    "kWh"
)

print(
    "Difference:",
    abs(energy_simpson - energy_trapezoid),
    "kWh"
)