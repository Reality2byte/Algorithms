# Define the Zaslavskii Map equations
def zaslavskii_map(x, p, F, n_iter=1000):
    x_values = [x]
    p_values = [p]
    for _ in range(n_iter):
        x_next = (x + p + F * np.sin(2 * np.pi * x)) % 1
        p_next = (p + F * np.sin(2 * np.pi * x_next)) % 1
        x_values.append(x_next)
        p_values.append(p_next)
        x, p = x_next, p_next
    return np.array(x_values), np.array(p_values)

# Metric for evaluating the "interestingness" and "beauty" of the plot
# For now, let's use the standard deviation of the x and p variables as a simple metric
def plot_metric(x, p):
    return np.std(x) + np.std(p)

# Test function to verify the dynamics of the Zaslavskii Map
def test_zaslavskii_map():
    # Parameters
    F = 0.55
    
    # Initial conditions
    x0, p0 = 0.1, 0.1
    
    # Number of iterations
    n_iter = 1000
    
    # Generate the Zaslavskii Map dynamics
    x_values, p_values = zaslavskii_map(x0, p0, F, n_iter=n_iter)
    
    # Plot the result
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Phase space (x, p)")
    plt.scatter(x_values, p_values, s=1)
    plt.xlabel("x")
    plt.ylabel("p")
    
    plt.subplot(1, 2, 2)
    plt.title("Time evolution")
    plt.plot(x_values, label="x")
    plt.plot(p_values, label="p")
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.legend()
    
    plt.show()
    
    # Compute and print the metric for "interestingness" and "beauty"
    metric = plot_metric(x_values, p_values)
    print(f"Plot Metric (Interestingness and Beauty): {metric}")
    
    # For a valid test, we expect the metric to be non-zero (the system should evolve)
    assert metric > 0, "Metric for interestingness and beauty should be greater than zero"

# Run the test
test_zaslavskii_map()
