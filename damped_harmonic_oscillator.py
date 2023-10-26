# Implementing and testing the Damped Harmonic Oscillator, which models oscillatory systems with damping (e.g., a swinging pendulum losing energy over time)
def damped_harmonic_oscillator(y, t, omega_0, gamma):
    """
    Equation of motion for a damped harmonic oscillator.
    y = [position, velocity]
    t = time
    omega_0 = natural frequency
    gamma = damping coefficient
    """
    position, velocity = y
    dydt = [velocity, -2 * gamma * omega_0 * velocity - omega_0**2 * position]
    return dydt

def test_damped_harmonic_oscillator():
    # Time span for the simulation
    t = np.linspace(0, 50, 500)
    
    # Initial conditions: position = 1, velocity = 0
    y0 = [1, 0]
    
    # Parameters: natural frequency omega_0 and damping coefficient gamma
    omega_0, gamma = 1.0, 0.1
    
    # Numerical solution using Euler's method
    dt = t[1] - t[0]
    y = np.empty((len(t), 2))
    y[0] = y0
    
    for i in range(1, len(t)):
        y[i] = y[i-1] + np.array(damped_harmonic_oscillator(y[i-1], t[i-1], omega_0, gamma)) * dt
    
    # Test: Checking if the system is damped
    # Qualitative test; we expect the amplitude of oscillation to decrease over time
    is_damped = np.max(y[-100:, 0]) < np.max(y[:100, 0])
    
    assert is_damped, "The system is not damped as expected."
    
    # Plotting the results
    plt.figure()
    plt.plot(t, y[:, 0], label="Position")
    plt.plot(t, y[:, 1], label="Velocity")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.title("Damped Harmonic Oscillator")
    plt.show()
    
    print("Test for Damped Harmonic Oscillator passed. The system shows damped oscillatory behavior.")

# Run the test function to verify the Damped Harmonic Oscillator
test_damped_harmonic_oscillator()
