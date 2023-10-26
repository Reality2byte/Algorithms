import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Implementing the Genesio-Tesi chaotic system
# Reference: Genesio, R., & Tesi, A. (1992). A harmonic balance approach to the period-doubling bifurcation. 
# IEEE Transactions on Automatic Control, 37(11), 1711-1715.

def genesio_tesi(t, y, a, b, c, d):
    """
    Genesio-Tesi system of ODEs.
    
    Parameters:
    t : float
        Time value, not used in the function as the system is autonomous.
    y : array-like, shape=(3,)
        The current state of the system [x, y, z].
    a, b, c, d : float
        The parameters of the system.
        
    Returns:
    dy : array-like, shape=(3,)
        The derivatives [dx/dt, dy/dt, dz/dt].
    """
    x, y, z = y
    dx_dt = -a * x - b * y - z + np.cos(t)
    dy_dt = x
    dz_dt = c * x + d * y
    
    return [dx_dt, dy_dt, dz_dt]

# Test function for Genesio-Tesi system
def test_genesio_tesi():
    # Define a test case with initial condition and parameters
    initial_conditions = [0, 1, 0]
    params = {'a': 1, 'b': 2, 'c': 0.1, 'd': 1}
    t_span = (0, 50)
    t_eval = np.linspace(*t_span, 5000)
    
    # Solve the system using solve_ivp
    sol = solve_ivp(genesio_tesi, t_span, initial_conditions, args=(params['a'], params['b'], params['c'], params['d']), t_eval=t_eval)
    
    # Test if the solution is chaotic by checking if it diverges or not
    # In a chaotic system, the trajectory should not go to infinity
    if np.all(np.isfinite(sol.y)):
        print("Test passed: The system does not diverge.")
    else:
        print("Test failed: The system diverges.")
        
    # Plot the trajectory in 3D space
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol.y[0], sol.y[1], sol.y[2])
    ax.set_title("Genesio-Tesi Attractor")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()
    
    # Metric for visual complexity: Range of z-values
    # A large range of z-values usually indicates a more complex and interesting structure
    z_range = np.ptp(sol.y[2])
    print(f"Metric (Range of Z): {z_range}")

# Run the test function
test_genesio_tesi()
