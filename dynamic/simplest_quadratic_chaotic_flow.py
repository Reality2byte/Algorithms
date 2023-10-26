import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the Simplest Quadratic Chaotic Flow
def simplest_quadratic_flow(state, t):
    x, y = state
    dxdt = y
    dydt = -x + y * (1 - x ** 2)
    return [dxdt, dydt]

# Test function for the Simplest Quadratic Chaotic Flow
def test_simplest_quadratic_flow():
    # Set initial conditions and time grid
    initial_conditions = [0.1, 0.1]
    t = np.linspace(0, 100, 10000)

    # Integrate the system of equations
    trajectory = odeint(simplest_quadratic_flow, initial_conditions, t)

    # Plot the trajectory in phase space
    plt.figure(figsize=(8, 8))
    plt.plot(trajectory[:, 0], trajectory[:, 1], lw=0.5)
    plt.title("Simplest Quadratic Chaotic Flow")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    # Compute a metric for the plot (Standard Deviation of x and y)
    std_x = np.std(trajectory[:, 0])
    std_y = np.std(trajectory[:, 1])

    # A higher standard deviation implies more "spread" and hence might be considered more "interesting"
    metric = std_x + std_y

    print(f"Plot metric (Standard Deviation of x + Standard Deviation of y): {metric}")
    assert metric > 1, "The plot does not meet the interestingness and beauty criteria"

# Run the test to generate the plot and compute the metric
test_simplest_quadratic_flow()

