import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sklearn.metrics import mean_squared_error

# Implementing the Chen's Canonical System
# Reference: Chen, Guanrong, and Ueta, T. "Yet another chaotic attractor", International Journal of Bifurcation and Chaos, 1999

def chens_canonical_system(Y, t, a=35, b=3, c=28):
    """
    Chen's Canonical System
    """
    x, y, z = Y
    dxdt = a * (y - x)
    dydt = (c - a) * x - x * z + c * y
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]

def test_chens_canonical_system():
    """
    Test function to validate the Chen's Canonical System
    """
    Y0 = [0, 2, 20]  # initial condition
    t = np.linspace(0, 1, 100)  # time points
    Y = odeint(chens_canonical_system, Y0, t)
    # Testing if the system is sensitive to initial conditions (a hallmark of chaotic systems)
    Y_alt = odeint(chens_canonical_system, [0.1, 2.1, 20.1], t)
    mse = mean_squared_error(Y, Y_alt)
    assert mse > 0.1, f"Test failed: MSE = {mse}"

# Run the test
test_chens_canonical_system()

# Simulation and Plotting
t = np.linspace(0, 100, 10000)
Y0 = [0, 2, 20]
Y = odeint(chens_canonical_system, Y0, t)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(Y[:, 0], Y[:, 1], Y[:, 2])
ax.set_title("Chen's Canonical System")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Metric to confirm "interestingness" and "beauty" (Mean Square Displacement)
msd = np.mean(np.square(np.diff(Y, axis=0)))
print(f"Mean Square Displacement for interestingness and beauty: {msd}")

plt.show()
