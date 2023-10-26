def harmonic_oscillation(A, omega, phi, t):
    """
    Calculate the harmonic oscillation.
    
    Parameters:
    A (float): amplitude
    omega (float): angular frequency
    phi (float): phase angle
    t (float): time
    
    Returns:
    float: position at time t
    """
    return A * np.cos(omega * t + phi)

def test_harmonic_oscillation():
    """
    Test the harmonic_oscillation function.
    """
    # Test case 1: A=1, omega=1, phi=0, t=0 should return 1
    assert np.isclose(harmonic_oscillation(1, 1, 0, 0), 1), "Test case 1 failed"
    
    # Test case 2: A=1, omega=1, phi=0, t=pi should return -1
    assert np.isclose(harmonic_oscillation(1, 1, 0, np.pi), -1), "Test case 2 failed"
    
    # Test case 3: A=2, omega=0, phi=0, t=10 should return 2
    assert np.isclose(harmonic_oscillation(2, 0, 0, 10), 2), "Test case 3 failed"
    
    print("All test cases passed")

# Run the test function
test_harmonic_oscillation()

# Plot the harmonic oscillation
t_values = np.linspace(0, 2 * np.pi, 100)
x_values = harmonic_oscillation(1, 1, 0, t_values)

plt.plot(t_values, x_values)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Harmonic Oscillation')
plt.grid(True)
plt.show()
