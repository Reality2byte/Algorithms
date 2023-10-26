def logistic_growth(P0, r, K, t):
    """
    Calculate the logistic growth.
    
    Parameters:
    P0 (float): initial population
    r (float): rate of growth
    K (float): carrying capacity
    t (float): time
    
    Returns:
    float: population at time t
    """
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

def test_logistic_growth():
    """
    Test the logistic_growth function.
    """
    # Test case 1: P0=1, r=1, K=10, t=0 should return 1
    assert np.isclose(logistic_growth(1, 1, 10, 0), 1), "Test case 1 failed"
    
    # Test case 2: P0=1, r=1, K=10, t=10 should be close to 10
    assert np.isclose(logistic_growth(1, 1, 10, 10), 10, atol=1e-1), "Test case 2 failed"
    
    # Test case 3: P0=1, r=0, K=10, t=10 should return 1
    assert np.isclose(logistic_growth(1, 0, 10, 10), 1), "Test case 3 failed"
    
    print("All test cases passed")

# Run the test function
test_logistic_growth()

# Plot the logistic growth
t_values = np.linspace(0, 10, 100)
P_values = logistic_growth(1, 1, 10, t_values)

plt.plot(t_values, P_values)
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Logistic Growth')
plt.grid(True)
plt.show()
