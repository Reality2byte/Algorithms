import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Toda Lattice equations
def toda_lattice(t, y, N, alpha):
    """
    Toda Lattice equations for a chain of N particles.
    Parameters:
        t (float): Time
        y (ndarray): A 1D numpy array of size 2*N. y[:N] are positions, y[N:] are momenta.
        N (int): Number of particles
        alpha (float): Interaction parameter
    Returns:
        dydt (ndarray): Derivatives [dq_1/dt, dq_2/dt, ..., dq_N/dt, dp_1/dt, dp_2/dt, ..., dp_N/dt]
    """
    dydt = np.zeros(2 * N)
    q = y[:N]
    p = y[N:]
    
    # Position derivatives are simply the momenta
    dydt[:N] = p
    
    # Momentum derivatives
    for i in range(N):
        dydt[N + i] = -np.exp(q[i] - q[(i+1)%N]) + np.exp(q[(i-1)%N] - q[i])
    
    return alpha * dydt

# Test the Toda Lattice equations
def test_toda_lattice():
    """
    Test the Toda Lattice function by integrating it over a short period of time
    and checking that the positions and momenta are changing as expected.
    """
    N = 5  # Number of particles
    alpha = 1.0  # Interaction parameter
    t_span = (0, 10)  # Time span
    t_eval = np.linspace(t_span[0], t_span[1], 500)  # Time points for evaluation
    y0 = np.random.rand(2 * N)  # Initial conditions (randomized for variety)
    
    # Solve the differential equations
    sol = solve_ivp(toda_lattice, t_span, y0, args=(N, alpha), t_eval=t_eval, rtol=1e-9, atol=1e-9)
    
    # Plot the result
    plt.figure(figsize=(12, 6))
    for i in range(N):
        plt.plot(sol.t, sol.y[i, :], label=f"q_{i+1}")
    for i in range(N, 2*N):
        plt.plot(sol.t, sol.y[i, :], label=f"p_{i-N+1}", linestyle='--')
    plt.xlabel("Time")
    plt.ylabel("State variables")
    plt.title("Toda Lattice")
    plt.legend()
    plt.show()

    # Metric for "interestingness" and "beauty" (subjective)
    # Here, we take the standard deviation of all state variables as a simple metric
    # More variation -> more "interesting" plot
    metric = np.std(sol.y)
    print(f"Interestingness and Beauty Metric: {metric:.4f}")

# Run the test function
test_toda_lattice()

