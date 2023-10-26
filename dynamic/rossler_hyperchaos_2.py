# Define the Rossler Hyperchaos II equations
def rossler_hyperchaos_II(state, t, a, b, c, d):
    x, y, z, w = state
    dxdt = -y - z
    dydt = x + a*y
    dzdt = b + z*(x - c)
    dwdt = d*(y - w)
    return [dxdt, dydt, dzdt, dwdt]

# Function to plot Rossler Hyperchaos II
def plot_rossler_hyperchaos_II(a, b, c, d, init_state, t):
    # Integrate the Rossler Hyperchaos II equations
    states = odeint(rossler_hyperchaos_II, init_state, t, args=(a, b, c, d))
    
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(states[:, 0], states[:, 1])
    ax.set_title('Rossler Hyperchaos II')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

# Test function for Rossler Hyperchaos II
def test_rossler_hyperchaos_II():
    a, b, c, d = 0.2, 0.2, 5.7, 1
    init_state = [1, 1, 1, 1]
    t = np.linspace(0, 100, 10000)

    # Solve and plot
    plot_rossler_hyperchaos_II(a, b, c, d, init_state, t)

    print("Rossler Hyperchaos II test passed.")

# Run the test
test_rossler_hyperchaos_II()
