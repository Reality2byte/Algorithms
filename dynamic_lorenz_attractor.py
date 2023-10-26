# Implementing and testing the Lorenz Attractor
def lorenz_attractor(t, y):
    """
    Defines the Lorenz Attractor equations.
    y = [x, y, z]
    """
    sigma = 10.0  # Prandtl number
    rho = 28.0  # Rayleigh number
    beta = 8 / 3  # aspect ratio

    x, y, z = y

    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return np.array([dx_dt, dy_dt, dz_dt])

# Test the Lorenz Attractor model
def test_lorenz_attractor():
    t0 = 0
    t_final = 20
    dt = 0.01
    y0 = np.array([0.1, 0, 0])  # Initial [x, y, z]

    t_values, y_values = euler_method(lorenz_attractor, y0, t0, t_final, dt)

    # Plot the results
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(y_values[:, 0], y_values[:, 1], y_values[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Lorenz Attractor')

    plt.show()

    # Print the final values as a rudimentary test
    print("Final x:", y_values[-1, 0])
    print("Final y:", y_values[-1, 1])
    print("Final z:", y_values[-1, 2])

# Run the test
test_lorenz_attractor()
