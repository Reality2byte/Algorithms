# Ueda Oscillator Model
def ueda_oscillator(state, t, alpha, beta, gamma):
    x, y = state
    dxdt = y
    dydt = -x - alpha * y - beta * x * (1 + gamma * x**2)
    return [dxdt, dydt]

# Test function for Ueda Oscillator
def test_ueda_oscillator():
    # Parameters
    alpha = 0.05
    beta = 1.0
    gamma = 0.1
    t = np.linspace(0, 50, 1000)
    initial_state = [0.1, 0.1]
    
    # Simulate
    trajectory = odeint(ueda_oscillator, initial_state, t, args=(alpha, beta, gamma))
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(trajectory[:, 0], trajectory[:, 1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ueda Oscillator')
    plt.show()
    
    # Metric: Standard Deviation of both x and y variables to ensure non-trivial dynamics
    std_devs = np.std(trajectory, axis=0)
    print(f"Standard Deviations of x and y variables: {std_devs}")
    assert np.all(std_devs > 0.1), "The system does not exhibit sufficiently interesting dynamics."
    print("Test passed. The system exhibits interesting and complex dynamics.")

# Run the test
test_ueda_oscillator()
