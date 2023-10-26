# Implementing and testing the Tent Map
# The tent map is a piecewise linear, one-dimensional map that also exhibits chaotic behavior.

def tent_map(x, mu):
    if x < 0.5:
        return mu * x
    else:
        return mu * (1 - x)

def test_tent_map():
    # Initial condition and parameter
    x = 0.5
    mu = 2.0
    
    # Time steps
    n = 100
    
    # Storing trajectory
    trajectory = [x]
    
    # Generate the trajectory
    for _ in range(n):
        x = tent_map(x, mu)
        trajectory.append(x)
    
    # Check if the system is producing the expected output (x should be bounded between 0 and 1)
    assert np.all((np.array(trajectory) >= 0) & (np.array(trajectory) <= 1)), "System is not bounded."
    
    # Plotting
    plt.figure(figsize=(10, 4))
    
    plt.plot(range(n+1), trajectory)
    plt.title("Tent Map")
    plt.xlabel("Time step")
    plt.ylabel("X")
    
    plt.tight_layout()
    plt.show()
    
    print("Test passed for Tent Map.")

# Run the test
test_tent_map()
