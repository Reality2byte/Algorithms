import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Implementing the SIR model dynamic system
def sir_model(Y, t, beta, gamma):
    """
    SIR model differential equations.
    Y: list of variables [S, I, R]
    t: time
    beta: infection rate
    gamma: recovery rate
    """
    S, I, R = Y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]

# Test function for SIR model
def test_sir_model():
    # Initial conditions: 90% susceptible, 10% infected, 0% recovered
    Y0 = [0.9, 0.1, 0]
    
    # Time grid for integration
    t = np.linspace(0, 160, 160)
    
    # Parameters: infection rate = 3.0, recovery rate = 1.0
    beta, gamma = 3.0, 1.0
    
    # Solve the differential equations
    solution = odeint(sir_model, Y0, t, args=(beta, gamma))
    S, I, R = solution.T

    # Plotting
    plt.figure()
    plt.plot(t, S, label="Susceptible")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recovered")
    plt.title("SIR Model")
    plt.xlabel("Time")
    plt.ylabel("Proportion")
    plt.legend()
    plt.show()

    # Test: Check if the sum S + I + R remains constant (=1) throughout
    total = S + I + R
    assert np.allclose(total, 1.0, atol=1e-6), "Total population should remain constant"
    print("SIR model test passed. Total population remains constant.")
    
# Run the test
test_sir_model()
