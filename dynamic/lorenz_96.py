# Define the Lorenz 96 equations
def lorenz_96(state, t, F):
    N = len(state)
    dxdt = np.zeros(N)
    for i in range(N):
        dxdt[i] = (state[(i - 1) % N] - state[(i + 2) % N]) * state[(i + 1) % N] - state[i] + F
    return dxdt

# Function to plot Lorenz 96 model
def plot_lorenz_96(F, init_state, t):
    # Integrate the Lorenz 96 equations
    states = odeint(lorenz_96, init_state, t, args=(F,))
    
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(states[:, 0], states[:, 1])
    ax.set_title('Lorenz 96 Model')
    ax.set_xlabel('x_0')
    ax.set_ylabel('x_1')
    plt.show()

# Test function for Lorenz 96 model
def test_lorenz_96():
    F = 8
    init_state = np.random.rand(5)
    t = np.linspace(0, 10, 1000)

    # Solve and plot
    plot_lorenz_96(F, init_state, t)

    print("Lorenz 96 model test passed.")

# Run the test
test_lorenz_96()
