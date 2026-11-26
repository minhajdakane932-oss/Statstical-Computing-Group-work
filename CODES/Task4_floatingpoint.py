import numpy as np

a = 0.1
b = 0.2
c = 0.3

result = a + b

print("Result:", result)
print("Exact equality:", result == c)

print("Approximately equal:",
      np.isclose(result, c))

# Calculate numerical error
actual = np.sqrt(2)
approximate = 1.414

absolute_error = abs(actual - approximate)

relative_error = absolute_error / abs(actual)

print("Actual value:", actual)
print("Approximate value:", approximate)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)