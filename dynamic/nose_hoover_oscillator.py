# Implementation of the Nose-Hoover Oscillator
# Reference: Hoover, W. G. (1985). Canonical dynamics: Equilibrium phase-space distributions.
# Physical review A, 31(3), 1695.

def nose_hoover(y, t, alpha, omega_0):
    """
    Compute the derivatives for the Nose-Hoover oscillator equations.
    
    Parameters:
        y (list): List of current [x, p, z] variables
        t (float): Time variable (unused, but required for odeint)
        alpha (float): Parameter alpha
        omega_0 (float): Natural frequency omega_0
    
    Returns:
        list: Derivatives [dx/dt, dp/dt, dz/dt]
    """
    x, p, z = y
    dx_dt = p
    dp_dt = -omega_0**2 * x - alpha * p * z
    dz_dt = alpha * (p**2 - 1)
    return [dx_dt, dp_dt, dz_dt]

def simulate_nose_hoover(initial_conditions, alpha, omega_0, t_max, dt):
    """
    Simulate the Nose-Hoover oscillator using odeint.
    
    Parameters:
        initial_conditions (list): Initial [x, p, z] variables
        alpha (float): Parameter alpha
        omega_0 (float): Natural frequency omega_0
        t_max (float): Maximum time for simulation
        dt (float): Time step size
    
    Returns:
        np.ndarray: Time points
        np.ndarray: Solution array of shape (len(t), 3)
    """
    t = np.arange(0, t_max, dt)
    solution = odeint(nose_hoover, initial_conditions, t, args=(alpha, omega_0))
    return t, solution

def plot_nose_hoover(t, solution):
    """
    Plot the Nose-Hoover oscillator.
    
    Parameters:
        t (np.ndarray): Time points
        solution (np.ndarray): Solution array of shape (len(t), 3)
    """
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))
    
    axs[0].plot(t, solution[:, 0])
    axs[0].set_title("Nose-Hoover Oscillator: x(t)")
    axs[0].set_xlabel("Time")
    axs[0].set_ylabel("x")
    
    axs[1].plot(t, solution[:, 1])
    axs[1].set_title("Nose-Hoover Oscillator: p(t)")
    axs[1].set_xlabel("Time")
    axs[1].set_ylabel("p")
    
    axs[2].plot(t, solution[:, 2])
    axs[2].set_title("Nose-Hoover Oscillator: z(t)")
    axs[2].set_xlabel("Time")
    axs[2].set_ylabel("z")
    
    plt.tight_layout()
    plt.show()

def test_nose_hoover():
    """
    Test the Nose-Hoover system by simulating and plotting it.
    """
    initial_conditions = [1.0, 0.0, 0.0]
    alpha, omega_0 = 1.0, 1.0
    t_max, dt = 50, 0.01
    t, solution = simulate_nose_hoover(initial_conditions, alpha, omega_0, t_max, dt)
    
    # For this dynamic system, we don't have a formal way to 'test' its behavior.
    # However, we can check if it returns a solution array of the expected shape and plot it.
    assert solution.shape == (len(t), 3), "Output shape mismatch"
    
    print("Test passed. Now plotting the Nose-Hoover Oscillator...")
    plot_nose_hoover(t, solution)

# Run the test
test_nose_hoover()
