import numpy as np
import timeit

# Generate one million values
data = np.random.rand(1000000)

# Using a normal Python loop
def normal_loop():
    result = []
    for value in data:
        result.append(value ** 2)
    return result

# Using NumPy vectorization
def vectorized():
    return data ** 2

# Measure execution time
loop_time = timeit.timeit(
    normal_loop, number=1
)

vector_time = timeit.timeit(
    vectorized, number=1
)

print("Loop execution time:", loop_time)
print("Vectorized execution time:", vector_time)

print("Speed-up:", loop_time / vector_time)