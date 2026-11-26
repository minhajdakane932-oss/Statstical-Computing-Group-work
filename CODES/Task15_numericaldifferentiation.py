import numpy as np
import matplotlib.pyplot as plt

# GPS readings
time = np.array(
    [0, 1, 2, 3, 4, 5, 6],
    dtype=float
)

position = np.array(
    [0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0]
)

speed = np.zeros_like(position)

# Forward difference
speed[0] = (
    position[1] - position[0]
) / (
    time[1] - time[0]
)

# Central differences
for i in range(1, len(time) - 1):

    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

for t, x, v in zip(time, position, speed):

    print(
        f"Time={t:.0f}s, "
        f"Position={x:.1f}m, "
        f"Speed={v:.2f}m/s"
    )

plt.plot(time, speed, marker="o")

plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS data")

plt.grid(True)
plt.show()