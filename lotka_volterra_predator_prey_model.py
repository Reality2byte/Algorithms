# Importing necessary libraries for numerical computation and plotting
import numpy as np
import matplotlib.pyplot as plt

# Implementing and testing the Lotka-Volterra model, which describes predator-prey interactions
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    """
    Lotka-Volterra equations for predator-prey model.
    y = [prey, predator]
    t = time
    alpha, beta, delta, gamma = model parameters
    """
    prey, predator = y
    dydt = [alpha*prey - beta*prey*predator, delta*prey*predator - gamma*predator]
    return dydt

def test_lotka_volterra():
    # Time span for the simulation
    t = np.linspace(0, 20, 500)
    
    # Initial conditions: 40 prey and 9 predators
    y0 = [40, 9]
    
    # Parameters alpha, beta, delta, gamma
    alpha, beta, delta, gamma = 0.1, 0.02, 0.01, 0.1
    
    # Numerical solution using Euler's method
    dt = t[1] - t[0]
    y = np.empty((len(t), 2))
    y[0] = y0
    
    for i in range(1, len(t)):
        y[i] = y[i-1] + np.array(lotka_volterra(y[i-1], t[i-1], alpha, beta, delta, gamma)) * dt
    
    # Test: Checking if prey and predator populations are oscillating
    # This is a qualitative test; we expect both populations to oscillate over time
    is_oscillating_prey = np.max(y[:, 0]) > np.min(y[:, 0]) * 1.5
    is_oscillating_predator = np.max(y[:, 1]) > np.min(y[:, 1]) * 1.5
    
    assert is_oscillating_prey and is_oscillating_predator, "The system is not oscillating as expected."
    
    # Plotting the results
    plt.figure()
    plt.plot(t, y[:, 0], label="Prey")
    plt.plot(t, y[:, 1], label="Predator")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.title("Lotka-Volterra Predator-Prey Model")
    plt.show()
    
    print("Test for Lotka-Volterra passed. The system shows oscillatory behavior for prey and predator populations.")

# Run the test function to verify the Lotka-Volterra model
test_lotka_volterra()

