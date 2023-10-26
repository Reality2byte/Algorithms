# Define the Duffing Oscillator equations
def duffing_oscillator(t, Y, alpha, beta, gamma, delta, omega):
    x, v = Y
    dxdt = v
    dvdt = gamma * np.cos(omega * t) - (delta * v + alpha * x + beta * x**3)
    return [dxdt, dvdt]

# Function to plot the Duffing Oscillator system
def plot_duffing_oscillator(Y, t):
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, Y[:, 0])
    plt.title('Duffing Oscillator')
    plt.xlabel('Time')
    plt.ylabel('x')
    
    plt.subplot(2, 1, 2)
    plt.plot(Y[:, 0], Y[:, 1])
    plt.xlabel('x')
    plt.ylabel('v')
    
    plt.tight_layout()
    plt.show()

# Test function for Duffing Oscillator
def test_duffing_oscillator():
    alpha = -1.0
    beta = 1.0
    gamma = 0.37
    delta = 0.3
    omega = 1.2
    Y0 = [0.1, 0.0]  # Initial conditions
    t = np.linspace(0, 100, 10000)  # Time array

    # Integrate the differential equations
    Y = odeint(duffing_oscillator, Y0, t, args=(alpha, beta, gamma, delta, omega), tfirst=True)

    # Check if the system is producing expected outputs (in this case, we check if it's non-zero)
    assert np.all(Y[-1000:] != 0), "The system output should not be all zeros."
    print("Test passed for Duffing Oscillator.")

    # Plotting
    plot_duffing_oscillator(Y, t)

# Run the test
test_duffing_oscillator()
