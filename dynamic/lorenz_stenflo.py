# Define the Lorenz-Stenflo equations
def lorenz_stenflo(t, y, sigma, rho, beta, mu):
    """
    Lorenz-Stenflo equations.
    Parameters:
        t (float): Time
        y (ndarray): A 1D numpy array of size 3. [x, y, z]
        sigma (float): Parameter
        rho (float): Parameter
        beta (float): Parameter
        mu (float): Parameter for the additional nonlinearity
    Returns:
        dydt (ndarray): Derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = y
    dxdt = sigma * (y - x)
    dydt = rho * x - y - x * z + mu * x * y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])

# Test the Lorenz-Stenflo equations
def test_lorenz_stenflo():
    """
    Test the Lorenz-Stenflo function by integrating it over a short period of time
    and checking the resulting behavior.
    """
    sigma = 10.0
    rho = 28.0
    beta = 8.0 / 3.0
    mu = 1.0  # Additional parameter
    t_span = (0, 50)
    t_eval = np.linspace(t_span[0], t_span[1], 5000)
    y0 = [1.0, 1.0, 1.0]  # Initial conditions
    
    # Solve the differential equations
    sol = solve_ivp(lorenz_stenflo, t_span, y0, args=(sigma, rho, beta, mu), t_eval=t_eval, rtol=1e-9, atol=1e-9)
    
    # Plot the result
    plt.figure(figsize=(12, 6))
    plt.plot(sol.y[0, :], sol.y[1, :], label='x-y trajectory')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Lorenz-Stenflo Attractor")
    plt.legend()
    plt.show()

    # Metric for "interestingness" and "beauty"
    # Again, we take the standard deviation of all state variables as a simple metric
    metric = np.std(sol.y)
    print(f"Interestingness and Beauty Metric: {metric:.4f}")

# Run the test function
test_lorenz_stenflo()

