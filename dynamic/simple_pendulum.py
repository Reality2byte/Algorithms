# Implementing the Simple Pendulum System
# Equations:
# d(theta)/dt = omega
# d(omega)/dt = -g/l * sin(theta)
def simple_pendulum(Y, t, g, l):
    theta, omega = Y
    dthetadt = omega
    domegadt = -g/l * np.sin(theta)
    return [dthetadt, domegadt]

# Test function for Simple Pendulum System
def test_simple_pendulum():
    # Parameters
    g, l = 9.81, 1.0  # gravitational constant and length of pendulum
    initial_conditions = [np.pi / 4, 0]  # initial angle and angular velocity
    t = np.linspace(0, 10, 500)
    
    # Integrate the equations
    solution = odeint(simple_pendulum, initial_conditions, t, args=(g, l))
    
    # Plot the results
    plt.figure()
    plt.title("Simple Pendulum System")
    plt.xlabel("Time")
    plt.ylabel("State Variables")
    plt.plot(t, solution[:, 0], label=r'\(\theta\) (angle)')
    plt.plot(t, solution[:, 1], label=r'\(\omega\) (angular velocity)')
    plt.legend()
    plt.show()

    # Check if the system produces non-trivial dynamics (i.e., not converging to a single point)
    assert np.std(solution[-100:, 0]) > 0.1
    assert np.std(solution[-100:, 1]) > 0.1

    print("Simple Pendulum Test Passed!")

# Run the test
test_simple_pendulum()
