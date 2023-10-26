# Implementing and testing the Van der Pol oscillator
def van_der_pol(t, y):
    """
    Defines the Van der Pol oscillator equations.
    y = [x, v] where x is position and v is velocity
    """
    mu = 1.0

    x, v = y

    dx_dt = v
    dv_dt = mu * (1 - x ** 2) * v - x

    return np.array([dx_dt, dv_dt])

# Test the Van der Pol oscillator
def test_van_der_pol():
    t0 = 0
    t_final = 50
    dt = 0.1
    y0 = np.array([2.0, 0])  # Initial [x, v]

    t_values, y_values = euler_method(van_der_pol, y0, t0, t_final, dt)

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t_values, y_values[:, 0], label='Position (x)')
    plt.plot(t_values, y_values[:, 1], label='Velocity (v)')
    plt.xlabel('Time')
    plt.ylabel('State')
    plt.legend()
    plt.title('Van der Pol Oscillator Time Series')

    plt.subplot(1, 2, 2)
    plt.plot(y_values[:, 0], y_values[:, 1])
    plt.xlabel('Position (x)')
    plt.ylabel('Velocity (v)')
    plt.title('Van der Pol Oscillator Phase Space')

    plt.tight_layout()
    plt.show()

    # Print the final values as a rudimentary test
    print("Final position:", y_values[-1, 0])
    print("Final velocity:", y_values[-1, 1])

# Run the test
test_van_der_pol()
