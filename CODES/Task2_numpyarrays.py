import numpy as np

# Hourly temperature readings
temperature = np.array([
    22.5, 23.0, 24.2, 25.1,
    26.0, 27.3, 28.1, 29.4
])

average = np.mean(temperature)
minimum = np.min(temperature)
maximum = np.max(temperature)

print("Average temperature:", average)
print("Minimum temperature:", minimum)
print("Maximum temperature:", maximum)

# Convert Celsius to Fahrenheit
fahrenheit = (temperature * 9/5) + 32

print("Temperatures in Fahrenheit:", fahrenheit)