# Implementing and testing the Tinkerbell Map
# The Tinkerbell map is a two-dimensional map that can display chaotic behavior.

def tinkerbell_map(state, a, b, c, d):
    x, y = state
    x_next = x**2 - y**2 + a*x + b*y
    y_next = 2*x*y + c*x + d*y
    return [x_next, y_next]

def test_tinkerbell_map():
    # Initial condition and parameters
    initial_state = [0.1, 0.1]
    a, b, c, d = 0.9, -0.6013, 2.0, 0.5
    
    # Time steps
    n = 100
    
    # Storing trajectory
    trajectory = [initial_state]
    
    # Generate the trajectory
    state = initial_state
    for _ in range(n):
        state = tinkerbell_map(state, a, b, c, d)
        trajectory.append(state)
    
    trajectory = np.array(trajectory)
    
    # Check if the system is producing the expected output (x, y should be bounded)
    assert np.all(np.abs(trajectory) < 100), "System is not bounded."
    
    # Plotting
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    
    ax[0].plot(range(n+1), trajectory[:, 0])
    ax[0].set_title("X vs Time step")
    ax[0].set_xlabel("Time step")
    ax[0].set_ylabel("X")
    
    ax[1].plot(range(n+1), trajectory[:, 1])
    ax[1].set_title("Y vs Time step")
    ax[1].set_xlabel("Time step")
    ax[1].set_ylabel("Y")
    
    plt.tight_layout()
    plt.show()
    
    print("Test passed for Tinkerbell Map.")

# Run the test
test_tinkerbell_map()
