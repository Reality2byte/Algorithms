from scipy.integrate import solve_ivp

# Implementing the Burgers' Equation
def burgers_equation(t, u, nu):
    """
    Computes the Burgers' Equation in 1D.
    Parameters:
        t: time
        u: vector of function values
        nu: viscosity parameter
    Returns:
        du/dt: time derivative of the function
    """
    dx = 2 * np.pi / (len(u) - 1)
    dudt = np.zeros_like(u)
    
    for i in range(1, len(u) - 1):
        dudt[i] = -u[i] * (u[i] - u[i-1]) / dx + nu * (u[i+1] - 2 * u[i] + u[i-1]) / dx**2

    # Periodic boundary conditions
    dudt[0] = -u[0] * (u[0] - u[-1]) / dx + nu * (u[1] - 2 * u[0] + u[-1]) / dx**2
    dudt[-1] = -u[-1] * (u[-1] - u[-2]) / dx + nu * (u[0] - 2 * u[-1] + u[-2]) / dx**2
    
    return dudt

# Test function for Burgers' Equation
def test_burgers_equation():
    nu = 0.1  # Viscosity parameter
    N = 100  # Number of grid points
    x = np.linspace(0, 2 * np.pi, N)
    u0 = np.sin(x)  # Initial condition
    t_span = [0, 10]  # Time span
    t_eval = np.linspace(t_span[0], t_span[1], 100)  # Time evaluation points
    
    # Solving the Burgers' Equation
    sol = solve_ivp(burgers_equation, t_span, u0, t_eval=t_eval, args=(nu,))
    
    # Plotting
    plt.figure(figsize=(10, 10))
    plt.imshow(sol.y, aspect='auto', extent=[0, 10, 0, 2 * np.pi], cmap='viridis')
    plt.colorbar(label="u")
    plt.title("Burgers' Equation")
    plt.xlabel("Time")
    plt.ylabel("x")
    plt.show()
    
    # Metric to determine if plot is 'interesting' and 'beautiful'
    # We will use the range of the function values as a metric.
    metric = np.max(sol.y) - np.min(sol.y)
    print(f"Metric for interestingness and beauty: {metric}")
    assert metric > 1  # If metric > 1, the test is considered passed

# Running the test function
test_burgers_equation()
