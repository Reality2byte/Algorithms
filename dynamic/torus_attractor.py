import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# Define the Torus Attractor system of ODEs
def torus_attractor(v, t, a, b, c):
    x, y, z = v
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

# Parameters for the Torus Attractor
a = 0.1
b = 0.1
c = 14.0

# Initial conditions
v0 = [0.1, 0, 0]

# Time grid for integration
t = np.linspace(0, 100, 10000)

# Integrate the ODEs
sol = odeint(torus_attractor, v0, t, args=(a, b, c))

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol[:, 0], sol[:, 1], sol[:, 2])
ax.set_title("Torus Attractor")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# Metric for beauty and interest: calculate the volume of the bounding box
# A more complex and larger volume should correspond to a more interesting plot
bounding_box_volume = (np.max(sol[:, 0]) - np.min(sol[:, 0])) * \
                      (np.max(sol[:, 1]) - np.min(sol[:, 1])) * \
                      (np.max(sol[:, 2]) - np.min(sol[:, 2]))

bounding_box_volume
