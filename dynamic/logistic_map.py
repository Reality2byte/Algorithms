# Implementing and testing the Bifurcation Logistic Map
# The logistic map is a one-dimensional difference equation that can exhibit complex, chaotic behavior.

def logistic_map(x, r):
    return r * x * (1 - x)

def test_logistic_map():
    # Initial condition and parameter
    x = 0.5
    r = 3.9
    
    # Time steps
    n = 100
    
    # Storing trajectory
    trajectory = [x]
    
    # Generate the trajectory
    for _ in range(n):
        x = logistic_map(x, r)
        trajectory.append(x)
    
    # Check if the system is producing the expected output (x should be bounded between 0 and 1)
    assert np.all((np.array(trajectory) >= 0) & (np.array(trajectory) <= 1)), "System is not bounded."
    
    # Plotting
    plt.figure(figsize=(10, 4))
    
    plt.plot(range(n+1), trajectory)
    plt.title("Logistic Map")
    plt.xlabel("Time step")
    plt.ylabel("X")
    
    plt.tight_layout()
    plt.show()
    
    print("Test passed for Bifurcation Logistic Map.")

# Run the test
test_logistic_map()
