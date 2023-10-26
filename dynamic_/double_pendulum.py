# Implementing and testing the Double Pendulum System
def double_pendulum(t, y):
    """
    Defines the Double Pendulum equations of motion.
    y = [theta1, omega1, theta2, omega2]
    """
    g = 9.81  # acceleration due to gravity
    l1 = 1.0  # length of the first pendulum
    l2 = 1.0  # length of the second pendulum
    m1 = 1.0  # mass of the first pendulum
    m2 = 1.0  # mass of the second pendulum

    theta1, omega1, theta2, omega2 = y

    delta_theta = theta2 - theta1

    # Equations of motion
    numerator1 = (m2 * l2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta)
                  + m2 * g * np.sin(theta2) * np.cos(delta_theta)
                  + m2 * l2 * omega2 ** 2 * np.sin(delta_theta)
                  - m1 * g * np.sin(theta1))
    
    denominator1 = (l1 * (m1 + m2) - m2 * l1 * np.cos(delta_theta) ** 2)
    
    numerator2 = (-l1 * omega1 ** 2 * np.sin(delta_theta) * np.cos(delta_theta)
                  + (m1 + m2) * g * np.sin(theta1)
                  - m2 * g * np.sin(theta1) * np.cos(delta_theta)
                  - l1 * omega1 ** 2 * np.sin(delta_theta))
    
    denominator2 = (l2 * (m1 + m2) - m2 * l2 * np.cos(delta_theta) ** 2)

    dtheta1_dt = omega1
    domega1_dt = numerator1 / denominator1
    dtheta2_dt = omega2
    domega2_dt = numerator2 / denominator2

    return np.array([dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt])

# Test the Double Pendulum model
def test_double_pendulum():
    t0 = 0
    t_final = 50
    dt = 0.05
    y0 = np.array([np.pi / 4, 0, np.pi / 4, 0])  # Initial [theta1, omega1, theta2, omega2]

    t_values, y_values = euler_method(double_pendulum, y0, t0, t_final, dt)

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t_values, y_values[:, 0], label='Theta 1')
    plt.plot(t_values, y_values[:, 2], label='Theta 2')
    plt.xlabel('Time')
    plt.ylabel('Angle (radians)')
    plt.legend()
    plt.title('Double Pendulum Angles Time Series')

    plt.subplot(1, 2, 2)
    plt.plot(y_values[:, 0], y_values[:, 1], label='Pendulum 1')
    plt.plot(y_values[:, 2], y_values[:, 3], label='Pendulum 2')
    plt.xlabel('Angle (radians)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.legend()
    plt.title('Double Pendulum Phase Space')

    plt.tight_layout()
    plt.show()

    # Print the final values as a rudimentary test
    print("Final theta1:", y_values[-1, 0])
    print("Final omega1:", y_values[-1, 1])
    print("Final theta2:", y_values[-1, 2])
    print("Final omega2:", y_values[-1, 3])

# Run the test
test_double_pendulum()
