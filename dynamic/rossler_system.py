import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Implementing the Rössler system
def rossler_system(state, t, a, b, c):
    x, y, z = state
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

# Test function for Rössler system
def test_rossler_system():
    a, b, c = 0.2, 0.2, 5.7
    initial_state = [1.0, 1.0, 1.0]
    t = np.linspace(0, 100, 10000)
    
    # Solving the system of ODEs
    solution = odeint(rossler_system, initial_state, t, args=(a, b, c))
    
    # Plotting the system
    plt.figure()
    plt.plot(t, solution[:, 0], label='x(t)')
    plt.plot(t, solution[:, 1], label='y(t)')
    plt.plot(t, solution[:, 2], label='z(t)')
    plt.title("Rössler system")
    plt.xlabel("Time")
    plt.ylabel("State variables")
    plt.legend()
    plt.show()

    # Test condition: check if the system is non-trivial (not constant)
    # We are expecting a chaotic system so the values shouldn't be constant
    assert not np.allclose(solution[0, :], solution[-1, :]), "The system seems to be trivial."
    print("Rössler system test passed.")

# Running the test
test_rossler_system()
