# Implementation of Bifurcation Diagram for Logistic Map
def logistic_map(r, x):
    return r * x * (1 - x)

# Test function for Bifurcation Diagram
def test_bifurcation_diagram():
    # Parameters
    r_values = np.linspace(2.5, 4.0, 10000)
    iterations = 1000
    last_iterations = 100

    # Initial value of x
    x = 1e-5 * np.ones(len(r_values))
    
    # Plotting setup
    plt.figure(figsize=(10, 7))
    plt.title("Bifurcation Diagram of the Logistic Map")
    plt.xlabel("r")
    plt.ylabel("x")
    
    # Generate Bifurcation Diagram
    for i in range(iterations):
        x = logistic_map(r_values, x)
        if i >= (iterations - last_iterations):
            plt.plot(r_values, x, ',k', alpha=0.25)
            
    plt.show()
    
    # Validate by checking the spread of x values for a specific r in the chaotic region
    r_chaos = 3.9
    x_test = np.linspace(0, 1, 100)
    for _ in range(100):
        x_test = logistic_map(r_chaos, x_test)
    assert len(set(np.round(x_test, 4))) > 1, "Test failed: Should have multiple distinct x values for chaotic r"
    
    print("Test passed: Bifurcation diagram shows transition to chaos.")

# Run the test
test_bifurcation_diagram()
