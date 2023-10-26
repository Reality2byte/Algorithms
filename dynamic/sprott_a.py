# Define the Sprott A attractor equations
def sprott_a(state, t):
    x, y, z = state
    dxdt = y
    dydt = -x + y * z
    dzdt = 1 - y**2
    return [dxdt, dydt, dzdt]

# Test function for the Sprott A attractor
def test_sprott_a():
    initial_state = [0, 2, 0]
    t = np.linspace(0, 100, 10000)
    
    # Solve the differential equations
    solution = odeint(sprott_a, initial_state, t)
    
    # Check if the trajectory stays bounded
    assert np.all(np.abs(solution) < 100), "The system does not seem to be bounded."
    
    # Plotting the attractor
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(solution[:, 0], solution[:, 1], solution[:, 2])
    ax.set_title("Sprott A Attractor")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()
    
    # Metric for "interestingness" and "beauty" could be the volume of the bounding box
    # occupied by the attractor.
    metric = np.prod(np.max(solution, axis=0) - np.min(solution, axis=0))
    print(f"Interestingness and Beauty Metric: {metric}")

# Run the test function for Sprott A Attractor
test_sprott_a()
