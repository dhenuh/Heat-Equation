import numpy as np
import matplotlib.pyplot as plt

L = 1.0
G = 100
dx = L / (G - 1)
alpha = 0.1
step = 0.0001



x = np.linspace(0, L, G)

u = np.zeros(G)


u[(x >= 0.4) & (x <= 0.6)] = 150.0


u[G-1] = u[G-2]
u[0] = u[1]

def compute_rates(unew):
    rate = np.zeros(G)
    for n in range(1, G - 1):
        rate[n] = alpha*(unew[n+1] - 2*unew[n]+ unew[n-1]) / dx**2
        rate[0] = alpha * (2 * unew[1] - 2 * unew[0]) / dx**2
        rate[G-1] = alpha * (2 * unew[G-2] - 2 * unew[G-1]) / dx**2

    return rate

def Euler_step(step):
    k1 = compute_rates(u)
    unew = u + step * k1
    return unew

def RK4_step(step):
    k1 = compute_rates(u)
    indice = u + (step/2) * k1
    k2 = compute_rates(indice)
    indice2 = u + (step/2) * k2
    k3 = compute_rates(indice2)
    indice3 = u + step * k3
    k4 = compute_rates(indice3)
    unew = u + (step/6) * (k1 + 2*k2 + 2*k3 + k4)
    return unew


fig = plt.figure()
ax = plt.axes(projection='3d')

total_steps = 40000
plot_steps = 4000
for i in range(1, total_steps + 1):
    u = RK4_step(step)
    time = i * step
    if(i % plot_steps == 0 or i == 1):
        ax.plot(x, [time] * len(x), u, label=f"Step {i} (t = {i*step:.3f}s)")



plt.legend()
ax.set_xlabel("Space")
ax.set_ylabel("Time")
ax.set_zlabel("U")
ax.set_title("MOL Heat Diffusion Profile")

plt.show()