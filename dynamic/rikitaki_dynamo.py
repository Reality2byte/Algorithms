import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Implementing the Rikitake Dynamo System
# Equations: 
# dx/dt = -y - z
# dy/dt = x + a * y
# dz/dt = b + z * (x - c)
def rikitake_dynamo(Y, t, a, b, c):
    x, y, z = Y
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

# Test function for Rikitake Dynamo System
def test_rikitake_dynamo():
    # Parameters
    a, b, c = 0.1, 0.1, 8.5
    initial_conditions = [0, 1, 1]
    t = np.linspace(0, 50, 5000)
    
    # Integrate the equations
    solution = odeint(rikitake_dynamo, initial_conditions, t, args=(a, b, c))
    
    # Plot the results
    plt.figure()
    plt.title("Rikitake Dynamo System")
    plt.xlabel("Time")
    plt.ylabel("State Variables")
    plt.plot(t, solution[:, 0], label='x')
    plt.plot(t, solution[:, 1], label='y')
    plt.plot(t, solution[:, 2], label='z')
    plt.legend()
    plt.show()

    # Check if the system produces non-trivial dynamics (i.e., not converging to a single point)
    assert np.std(solution[-1000:, 0]) > 0.1
    assert np.std(solution[-1000:, 1]) > 0.1
    assert np.std(solution[-1000:, 2]) > 0.1

    print("Rikitake Dynamo Test Passed!")

# Run the test
test_rikitake_dynamo()

