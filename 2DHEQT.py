import numpy as np
import matplotlib.pyplot as plt

alpha = 0.5
dt = 0.01
t_max = 2.0
num_steps = int(t_max / dt)
x = np.linspace(1, 10, num = 10)
y = np.linspace(1, 10, num = 10)
X, Y = np.meshgrid(x, y)
T = np.zeros((10, 10))
T[4 : 6, 4 : 6] = 100.0

peak_history = []
time_history = []


for step in range(num_steps):
    current_time = step * dt

    
    center = T[1:-1, 1:-1]
    up = T[:-2, 1:-1]
    down = T[2:, 1:-1]
    left = T[1:-1, :-2]
    right = T[1:-1, 2:]
#praise laplacian stencil
    curvature = up + down + left + right - 4 * center

   
    peak_history.append(T[5, 5])
    time_history.append(current_time)


    T[1:-1, 1:-1] = center + alpha * dt * curvature


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))


im = ax1.imshow(T, cmap="hot", extent=[0, 9, 0, 9], origin="lower")
ax1.set_title("Final Temperature State (t = 2.0s)")
ax1.set_xlabel("X coordinate")
ax1.set_ylabel("Y coordinate")
fig.colorbar(im, ax=ax1, label="Temperature")


ax2.plot(time_history, peak_history, color="red", linewidth=2)
ax2.set_title("Temperature of the Center Peak Over Time")
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Temperature")
ax2.grid(True, linestyle="--")

plt.tight_layout()
plt.show()
