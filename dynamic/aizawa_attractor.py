import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Aizawa Attractor
def aizawa_attractor(state, t):
    """
    Aizawa Attractor equations
    """
    x, y, z = state
    a, b, c, d, e, f = 0.95, 0.7, 0.6, 3.5, 0.25, 0.1  # Parameters
    
    dx = (z - b) * x - d * y
    dy = d * x + (z - b) * y
    dz = c + a * z - (z ** 3) / 3 - (x ** 2 + y ** 2) * (1 + e * z) + f * z * (x ** 3)
    
    return [dx, dy, dz]

# Initial state [x, y, z]
initial_state = [0.1, 0, 0]

# Time grid for integration
t = np.linspace(0, 100, 10000)

# Integrate the Aizawa equations over the time grid t
trajectory = odeint(aizawa_attractor, initial_state, t)

# Plotting the Aizawa Attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], lw=0.5)
ax.set_title("Aizawa Attractor")
plt.show()
