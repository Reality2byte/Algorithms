# Define the Newton-Leipnik System
def newton_leipnik_system(state, t):
    x, y, z = state
    dxdt = -0.4 * x + 2 * y - y * z
    dydt = -0.4 * y + x * z
    dzdt = 1 - x ** 2 - 0.1 * z
    return [dxdt, dydt, dzdt]

# Test function for the Newton-Leipnik System
def test_newton_leipnik_system():
    # Set initial conditions and time grid
    initial_conditions = [0.1, 0.1, 0.1]
    t = np.linspace(0, 100, 10000)

    # Integrate the system of equations
    trajectory = odeint(newton_leipnik_system, initial_conditions, t)

    # Plot the trajectory in 3D space
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], lw=0.5)
    ax.set_title("Newton-Leipnik System")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()

    # Compute a metric for the plot (Standard Deviation of x, y, and z)
    std_x = np.std(trajectory[:, 0])
    std_y = np.std(trajectory[:, 1])
    std_z = np.std(trajectory[:, 2])

    # A higher standard deviation implies more "spread" and hence might be considered more "interesting"
    metric = std_x + std_y + std_z

    print(f"Plot metric (Standard Deviation of x + Standard Deviation of y + Standard Deviation of z): {metric}")
    assert metric > 1, "The plot does not meet the interestingness and beauty criteria"

# Run the test to generate the plot and compute the metric
test_newton_leipnik_system()

