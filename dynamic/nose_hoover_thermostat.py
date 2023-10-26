import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def nose_hoover_thermostat(state, t, Q, T):
    """
    Nosé-Hoover Thermostat
    Parameters:
    - state: List of current [position, velocity, thermostat variable]
    - t: current time
    - Q: coupling strength
    - T: temperature
    """
    x, v, xi = state
    dxdt = v
    dvdt = -x - Q * xi * v
    dxidt = 1 / Q * (v ** 2 - T)
    
    return [dxdt, dvdt, dxidt]

# Test function to validate the Nosé-Hoover Thermostat
def test_nose_hoover_thermostat():
    Q = 1.0  # coupling strength
    T = 1.0  # temperature
    initial_state = [0.0, 1.0, 0.0]  # [position, velocity, thermostat variable]
    t = np.linspace(0, 100, 10000)  # time grid

    # Integrate the ODEs
    trajectory = odeint(nose_hoover_thermostat, initial_state, t, args=(Q, T))
    
    # Extract position, velocity, and thermostat variable for plotting
    x, v, xi = trajectory[:, 0], trajectory[:, 1], trajectory[:, 2]
    
    # Create plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(x, v, label='Nosé-Hoover Thermostat')
    ax.set_title("Nosé-Hoover Thermostat")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Velocity (v)")
    ax.legend()
    plt.show()

    # Compute metric for "interestingness" and "beauty" using standard deviation
    # A more spread-out trajectory might indicate a more interesting dynamic behavior
    metric = np.std(x) * np.std(v)
    print(f"Interestingness and Beauty Metric: {metric}")
    assert metric > 0, "The metric should be greater than zero for a non-trivial dynamic system."

# Run the test function to validate the model and plot the trajectory
test_nose_hoover_thermostat()
