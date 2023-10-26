# Implementing and testing the Rossler Attractor
def rossler_attractor(t, y):
    """
    Defines the Rossler Attractor equations.
    y = [x, y, z]
    """
    a = 0.2
    b = 0.2
    c = 5.7

    x, y, z = y

    dx_dt = -y - z
    dy_dt = x + a * y
    dz_dt = b + z * (x - c)

    return np.array([dx_dt, dy_dt, dz_dt])

# Test the Rossler Attractor model
def test_rossler_attractor():
    t0 = 0
    t_final = 100
    dt = 0.01
    y0 = np.array([1, 1, 1])  # Initial [x, y, z]

    t_values, y_values = euler_method(rossler_attractor, y0, t0, t_final, dt)

    # Plot the results
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(y_values[:, 0], y_values[:, 1], y_values[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rossler Attractor')

    plt.show()

    # Print the final values as a rudimentary test
    print("Final x:", y_values[-1, 0])
    print("Final y:", y_values[-1, 1])
    print("Final z:", y_values[-1, 2])

# Run the test
test_rossler_attractor()
