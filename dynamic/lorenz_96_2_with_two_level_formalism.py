# Define the Lorenz-96 II Model with two-level formalism equations
def lorenz_96_II(Y, t, F, K, J, h, c, b):
    # Separate the variables into two levels: X and Y
    X = Y[:K]
    Y = Y[K:]
    
    # Initialize derivatives
    dXdt = np.zeros(K)
    dYdt = np.zeros(K * J)
    
    # Compute derivatives for X
    for k in range(K):
        dXdt[k] = -X[k-1] * (X[k-2] - X[(k+1) % K]) - X[k] + F - h * np.sum(Y[k*J:(k+1)*J])
    
    # Compute derivatives for Y
    for j in range(K * J):
        k = j // J
        kp1 = (j + J) // J
        dYdt[j] = -c * b * Y[(j+1) % (K * J)] * (Y[(j+2) % (K * J)] - Y[j-1]) - c * Y[j] + h * X[k] / J
    
    return np.concatenate([dXdt, dYdt])

# Test function for the Lorenz-96 II Model with two-level formalism
def test_lorenz_96_II():
    # Parameters for the system
    F = 10
    K = 5
    J = 4
    h = 1
    c = 10
    b = 10
    
    # Initial conditions
    X0 = np.ones(K) * F
    Y0 = np.random.rand(K * J) * 0.01
    Y0 = np.concatenate([X0, Y0])
    
    # Time grid for integration
    t = np.linspace(0, 10, 1000)
    
    # Solve the ODE system
    solution = odeint(lorenz_96_II, Y0, t, args=(F, K, J, h, c, b))
    
    # Compute a metric for 'interestingness' and 'beauty' (here, we use the standard deviation of X-values as a simple metric)
    X_values = solution[:, :K]
    metric = np.std(X_values)
    
    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for k in range(K):
        ax.plot(t, solution[:, k], label=f'X_{k+1}')
    ax.set_title("Lorenz-96 II Model with Two-Level Formalism")
    ax.set_xlabel("Time")
    ax.set_ylabel("X Values")
    ax.legend()
    plt.show()
    
    # Check if the metric meets the criteria for 'interesting and beautiful' (here, arbitrarily chosen as 1)
    assert metric > 1, f"Metric value is {metric}, expected > 1"

    print(f"Test passed. Metric value: {metric}")

# Run the test function
test_lorenz_96_II()
