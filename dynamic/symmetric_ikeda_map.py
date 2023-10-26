def symmetric_ikeda_map(initial_conditions, mu, steps):
    """
    Simulate the Symmetric Ikeda Map.
    
    Parameters:
        initial_conditions (tuple): Initial conditions (x0, y0)
        mu (float): Parameter of the Symmetric Ikeda Map
        steps (int): Number of steps to simulate
    
    Returns:
        np.ndarray: Time series of shape (steps, 2)
    """
    # Initialize variables
    x, y = initial_conditions
    trajectory = np.zeros((steps, 2))
    
    # Time evolution
    for i in range(steps):
        trajectory[i] = [x, y]
        t = 0.4 - 6 / (1 + x ** 2 + y ** 2)
        x, y = 1 + mu * (x * np.cos(t) - y * np.sin(t)), mu * (x * np.sin(t) + y * np.cos(t))
    
    return trajectory

def plot_symmetric_ikeda_map(trajectory):
    """
    Plot the Symmetric Ikeda Map trajectory.
    
    Parameters:
        trajectory (np.ndarray): Time series of shape (steps, 2)
    """
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Time Series')
    plt.plot(trajectory[:, 0], label='x')
    plt.plot(trajectory[:, 1], label='y')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.title('Phase Space')
    plt.scatter(trajectory[:, 0], trajectory[:, 1], c=np.arange(len(trajectory)), cmap='viridis', s=5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def test_symmetric_ikeda_map():
    """
    Test the Symmetric Ikeda Map function by creating a trajectory and plotting it.
    """
    # Parameters for the Symmetric Ikeda Map
    initial_conditions = (0.1, 0.1)
    mu = 0.9
    steps = 1000
    
    # Generate and plot the trajectory
    trajectory = symmetric_ikeda_map(initial_conditions, mu, steps)
    plot_symmetric_ikeda_map(trajectory)
    
    # Metric for "interestingness" and "beauty": Standard deviation of x and y
    std_x = np.std(trajectory[:, 0])
    std_y = np.std(trajectory[:, 1])
    print(f"Standard deviation of x: {std_x}, Standard deviation of y: {std_y}")
    assert std_x > 0.1 and std_y > 0.1, "Plot is not sufficiently interesting."
    
test_symmetric_ikeda_map()
