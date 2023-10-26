import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t0, t_final, dt):
    """
    Implement the Euler method for solving first-order ODEs.
    """
    # Initialize variables
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0

    # Run Euler method
    while t < t_final:
        y = y + dt * f(t, y)
        t += dt
        t_values.append(t)
        y_values.append(y)

    return np.array(t_values), np.array(y_values)

# Implementing and testing the predator-prey model with Allee effect
def allee_predator_prey(t, y):
    """
    Defines the Allee effect predator-prey model.
    y = [prey_population, predator_population]
    """
    a = 0.1  # Allee threshold for prey
    r = 1.0  # Prey birth rate
    c = 0.01  # Predation rate
    m = 0.1  # Predator mortality rate
    e = 0.1  # Conversion efficiency

    prey, predator = y

    # Prey growth rate with Allee effect
    prey_growth = r * prey * (1 - prey) * (prey - a)
    # Predator growth rate
    predator_growth = e * c * prey * predator - m * predator

    return np.array([prey_growth, predator_growth])

# Test the Allee predator-prey model
def test_allee_predator_prey():
    t0 = 0
    t_final = 50
    dt = 0.1
    y0 = np.array([0.2, 0.1])  # Initial [prey, predator]

    t_values, y_values = euler_method(allee_predator_prey, y0, t0, t_final, dt)

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t_values, y_values[:, 0], label='Prey')
    plt.plot(t_values, y_values[:, 1], label='Predator')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.legend()
    plt.title('Allee Predator-Prey Model Time Series')

    plt.subplot(1, 2, 2)
    plt.plot(y_values[:, 0], y_values[:, 1])
    plt.xlabel('Prey')
    plt.ylabel('Predator')
    plt.title('Allee Predator-Prey Model Phase Space')

    plt.tight_layout()
    plt.show()

    # Print the final values as a rudimentary test
    print("Final prey population:", y_values[-1, 0])
    print("Final predator population:", y_values[-1, 1])

# Run the test
test_allee_predator_prey()
