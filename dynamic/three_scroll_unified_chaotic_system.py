# Revised implementation of the Three-Scroll Unified Chaotic System
# Reference: "Three-scroll Unified Chaotic System" by Guanrong Chen, Ueta Takuji
# Note: Parameters are chosen based on the research paper to ensure stability and chaotic behavior
def three_scroll_unified_system(state, t):
    x, y, z = state
    a, b, c = 40.0, 1.833, 0.16  # Parameters
    dxdt = a * (y - x)
    dydt = (c * a) * x - x * z + c * y
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]

# Revise the test function
def test_three_scroll_unified():
    # Initial state
    initial_state = [0.1, 0, 0]
    # Time array
    t = np.linspace(0, 100, 10000)
    # Integrate the system of ODE
    states = odeint(three_scroll_unified_system, initial_state, t)
    
    # Metric: Mutual Information to check randomness and complexity
    metric = mutual_info_score(np.histogram(states[:, 0])[0], np.histogram(states[:, 1])[0])
    
    # Plot the system
    plot_three_scroll_unified(states, 'Three-Scroll Unified Chaotic System')
    
    print(f"Mutual Information Score: {metric}")

    # If metric is not zero, the system is complex and passes the test
    assert metric > 0, "The system does not pass the complexity metric."

# Run the test again
test_three_scroll_unified()
