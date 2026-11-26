import numpy as np
from scipy.optimize import root_scalar

cash_flows = [-10000, 3000, 3500, 4000, 2500]

def npv(rate):
    return sum(
        cf / (1 + rate) ** t
        for t, cf in enumerate(cash_flows)
    )

def derivative(rate):
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

# Newton-Raphson
newton = root_scalar(
    npv,
    fprime=derivative,
    x0=0.10,
    method="newton"
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.15,
    method="secant"
)

print("Newton-Raphson rate:", newton.root)
print("Secant rate:", secant.root)
print("NPV at calculated rate:", npv(newton.root))