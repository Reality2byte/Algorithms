# Implementing and testing the Forced Damped Pendulum
def forced_damped_pendulum(state, t, alpha, beta, omega, A):
    """
    Forced Damped Pendulum Differential Equations
    """
    theta, omega_theta = state
    dthetadt = omega_theta
    domegadt = -alpha * omega_theta - beta * np.sin(theta) + A * np.cos(omega * t)
    return [dthetadt, domegadt]

def test_forced_damped_pendulum():
    """
    Test function for Forced Damped Pendulum
    """
    # Define the initial conditions and parameters
    initial_state = [0.1, 0.0]
    t = np.linspace(0, 100, 1000)
    alpha, beta, omega, A = 0.1, 1.0, 0.5, 0.5
    
    # Integrate the Forced Damped Pendulum equations on the time grid t
    solution = odeint(forced_damped_pendulum, initial_state, t, args=(alpha, beta, omega, A))
    
    # Print output for verification (first 5 entries)
    print("First 5 entries of Forced Damped Pendulum:")
    print(solution[:5])
    
    # Plot
    plt.figure()
    plt.plot(t, solution[:, 0], label='theta (Angle)')
    plt.plot(t, solution[:, 1], label='omega_theta (Angular velocity)')
    plt.legend()
    plt.title('Forced Damped Pendulum')
    plt.xlabel('Time')
    plt.ylabel('State Variables')
    plt.show()

# Run the test to make sure the dynamic system is producing the expected outputs
test_forced_damped_pendulum()
