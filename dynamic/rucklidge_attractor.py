# Define the Rucklidge equations
def rucklidge(t, y, k, m, lambda_):
    """
    Rucklidge equations.
    Parameters:
        t (float): Time
        y (ndarray): A 1D numpy array of size 3. [x, y, z]
        k (float): Parameter
        m (float): Parameter
        lambda_ (float): Parameter
    Returns:
        dydt (ndarray): Derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = y
    dxdt = lambda_ * (y - x)
    dydt = lambda_ * (m * x - k * y - x * z)
    dzdt = -z + x * y
    return np.array([dxdt, dydt, dzdt])

# Test the Rucklidge equations
def test_rucklidge():
    """
    Test the Rucklidge function by integrating it over a short period of time
    and checking the resulting behavior.
    """
    k = 2.0
    m = 1.0
    lambda_ = 6.7  # Parameters
    t_span = (0, 100)
    t_eval = np.linspace(t_span[0], t_span[1], 5000)
    y0 = [1.0, 1.0, 20.0]  # Initial conditions
    
    # Solve the differential equations
    sol = solve_ivp(rucklidge, t_span, y0, args=(k, m, lambda_), t_eval=t_eval, rtol=1e-9, atol=1e-9)
    
    # Plot the result
    plt.figure(figsize=(12, 6))
    plt.plot(sol.y[0, :], sol.y[2, :], label='x-z trajectory')
    plt.xlabel("x")
    plt.ylabel("z")
    plt.title("Rucklidge Attractor")
    plt.legend()
    plt.show()

    # Metric for "interestingness" and "beauty"
    # Once again, we take the standard deviation of all state variables as a simple metric
    metric = np.std(sol.y)
    print(f"Interestingness and Beauty Metric: {metric:.4f}")

# Run the test function
test_rucklidge()

