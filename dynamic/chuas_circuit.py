import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Chua's Circuit Equations
def chua_circuit(Y, t, alpha, beta, m0, m1):
    """
    Y = [x, y, z]
    alpha, beta, m0, m1 are the parameters of the Chua's circuit.
    """
    x, y, z = Y
    # Nonlinear function
    h_x = m1 * x + 0.5 * (m0 - m1) * (abs(x + 1) - abs(x - 1))
    # Equations
    dxdt = alpha * (y - x - h_x)
    dydt = x - y + z
    dzdt = -beta * y
    return [dxdt, dydt, dzdt]

# Test function for Chua's Circuit
def test_chua_circuit():
    # Parameters
    alpha = 9.0
    beta = 14.286
    m0 = -1.143
    m1 = -0.714
    # Initial conditions
    Y0 = [0.7, 0.0, 0.0]
    # Time array
    t = np.linspace(0, 100, 10000)
    # Solving the ODE
    solution = odeint(chua_circuit, Y0, t, args=(alpha, beta, m0, m1))
    # Plotting
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, solution[:, 0])
    plt.title("Chua's Circuit")
    plt.ylabel("x")
    plt.subplot(3, 1, 2)
    plt.plot(t, solution[:, 1])
    plt.ylabel("y")
    plt.subplot(3, 1, 3)
    plt.plot(t, solution[:, 2])
    plt.ylabel("z")
    plt.xlabel("Time")
    plt.show()
    # Test: Ensure that the system is not static (e.g., all zeros)
    assert not np.all(solution == 0)

# Run the test
test_chua_circuit()
