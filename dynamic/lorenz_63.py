# Re-importing the necessary libraries and re-running the code
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Lorenz '63 Attractor Model
def lorenz_63(state, t, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Test function for Lorenz '63 Attractor
def test_lorenz_63():
    # Parameters
    sigma = 10
    rho = 28
    beta = 8/3
    initial_state = [1.0, 1.0, 1.0]
    t = np.linspace(0, 50, 5000)
    
    # Solve differential equations
    trajectory = odeint(lorenz_63, initial_state, t, args=(sigma, rho, beta))
    
    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2])
    ax.set_title('Lorenz \'63 Attractor')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    
    # Validate by checking if trajectory deviates from initial condition (sign of chaos)
    final_state = trajectory[-1, :]
    assert not np.allclose(final_state, initial_state, atol=1e-1), "The system did not diverge from the initial state."
    
# Run the test
test_lorenz_63()
