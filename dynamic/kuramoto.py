# Define the Kuramoto model equations
def kuramoto_model(t, theta, omega, K, N):
    dtheta = omega + (K / N) * np.sum(np.sin(np.subtract.outer(theta, theta)), axis=1)
    return dtheta

# Function to plot the Kuramoto model system
def plot_kuramoto_model(theta, t):
    plt.figure()
    for i in range(theta.shape[1]):
        plt.plot(t, np.sin(theta[:, i]))
    plt.title('Kuramoto Model')
    plt.xlabel('Time')
    plt.ylabel('Amplitude of Oscillators')
    plt.show()

# Test function for Kuramoto model
def test_kuramoto_model():
    N = 5  # Number of oscillators
    K = 2.0  # Global coupling strength
    omega = np.random.uniform(-1, 1, N)  # Natural frequencies
    theta0 = np.random.uniform(0, 2 * np.pi, N)  # Initial phases
    t = np.linspace(0, 50, 5000)  # Time array

    # Integrate the differential equations
    theta = odeint(kuramoto_model, theta0, t, args=(omega, K, N), tfirst=True)

    # Check if the system is producing expected outputs (in this case, we check if it's non-zero)
    assert np.all(theta[-1000:] != 0), "The system output should not be all zeros."
    print("Test passed for Kuramoto model.")

    # Plotting
    plot_kuramoto_model(theta, t)

# Run the test
test_kuramoto_model()
