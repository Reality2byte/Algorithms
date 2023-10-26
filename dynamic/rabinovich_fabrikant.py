import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Implementing the Rabinovich–Fabrikant equations
# The Rabinovich–Fabrikant equations are a set of three first-order, 
# nonlinear, ordinary differential equations used to describe the time 
# evolution of complex systems. They are commonly used to model 
# chaotic systems and are given by:
#
# dx/dt = y * (z - 1 + x) + gamma * x
# dy/dt = x * (3 * z + 1 - x) + gamma * y
# dz/dt = -2 * z * (alpha + x * y)

def rabinovich_fabrikant(Y, t, alpha, gamma):
    x, y, z = Y
    dxdt = y * (z - 1 + x) + gamma * x
    dydt = x * (3 * z + 1 - x) + gamma * y
    dzdt = -2 * z * (alpha + x * y)
    return [dxdt, dydt, dzdt]

# Parameters
alpha = 0.1
gamma = 0.1

# Initial conditions
initial_conditions = [0.1, 0.1, 0.1]

# Time grid for integration
t = np.linspace(0, 100, 10000)

# Integrate the equations
solution = odeint(rabinovich_fabrikant, initial_conditions, t, args=(alpha, gamma))

# Plotting
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, solution[:, 0], label="x(t)")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, solution[:, 1], label="y(t)")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, solution[:, 2], label="z(t)")
plt.xlabel("Time")
plt.ylabel("z(t)")
plt.legend()

plt.tight_layout()
plt.show()

# Test function to verify the system
def test_rabinovich_fabrikant():
    # Integrate for a short time to get the next state
    t_test = np.linspace(0, 1, 10)
    test_solution = odeint(rabinovich_fabrikant, [0.1, 0.1, 0.1], t_test, args=(alpha, gamma))
    
    # Check if the system is not in a fixed point by making sure the state variables are changing
    dx = test_solution[-1, 0] - test_solution[0, 0]
    dy = test_solution[-1, 1] - test_solution[0, 1]
    dz = test_solution[-1, 2] - test_solution[0, 2]
    
    assert dx != 0 and dy != 0 and dz != 0, "The system is in a fixed point."
    
    print("Rabinovich–Fabrikant test passed.")

# Run the test
test_rabinovich_fabrikant()
