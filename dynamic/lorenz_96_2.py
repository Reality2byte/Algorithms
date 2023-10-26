# Re-attempting the implementation and test for Lorenz 96-II Model

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Lorenz 96-II Model
def lorenz_96_II(state, t, F, h, c, b, J):
    # Unpack state
    N = len(state) // (J + 1)
    x = state[:N]
    y = state[N:].reshape((N, J))
    
    # Initialize derivatives
    dxdt = np.zeros(N)
    dydt = np.zeros((N, J))
    
    # Compute dx/dt
    for i in range(N):
        dxdt[i] = -x[i - 1] * (x[i - 2] - x[(i + 1) % N]) - x[i] + F - h * np.sum(y[i, :])
    
    # Compute dy/dt
    for i in range(N):
        for j in range(J):
            dydt[i, j] = -c * b * y[i, (j + 1) % J] * (y[i, (j + 2) % J] - y[i, j - 1]) - c * y[i, j] + h * x[i] / J
    
    # Return flattened array of derivatives
    return np.concatenate((dxdt, dydt.flatten()))

# Test function
def test_lorenz_96_II():
    # Parameters
    F = 8.0
    h = 1.0
    c = 10.0
    b = 10.0
    J = 4
    N = 5
    t = np.linspace(0, 2, 500)
    initial_state = np.random.rand(N * (J + 1))
    
    # Simulate
    trajectory = odeint(lorenz_96_II, initial_state, t, args=(F, h, c, b, J))
    
    # Plotting
    plt.figure(figsize=(10, 6))
    for i in range(N):
        plt.plot(t, trajectory[:, i], label=f"x_{i+1}")
    plt.xlabel('Time')
    plt.ylabel('State Variables')
    plt.title('Lorenz 96-II Model')
    plt.legend()
    plt.show()
    
    # Metric: Standard Deviation of the x variables to ensure non-trivial dynamics
    std_devs = np.std(trajectory[:, :N], axis=0)
    print(f"Standard Deviations of x variables: {std_devs}")
    assert np.all(std_devs > 1.0), "The system does not exhibit sufficiently interesting dynamics."
    print("Test passed. The system exhibits interesting and complex dynamics.")

# Run the test
test_lorenz_96_II()
