def first_order_linear(y0, y_final, tau, t):
    """
    Calculate the first-order linear system response.
    
    Parameters:
    y0 (float): initial output
    y_final (float): final output
    tau (float): time constant
    t (float): time
    
    Returns:
    float: output at time t
    """
    return y0 + (y_final - y0) * (1 - np.exp(-t / tau))

def test_first_order_linear():
    """
    Test the first_order_linear function.
    """
    # Test case 1: y0=0, y_final=1, tau=1, t=0 should return 0
    assert np.isclose(first_order_linear(0, 1, 1, 0), 0), "Test case 1 failed"
    
    # Test case 2: y0=0, y_final=1, tau=1, t=1 should be close to 0.632
    assert np.isclose(first_order_linear(0, 1, 1, 1), 0.632, atol=1e-3), "Test case 2 failed"
    
    # Test case 3: y0=0, y_final=1, tau=1, t=10 should be close to 1
    assert np.isclose(first_order_linear(0, 1, 1, 10), 1, atol=1e-3), "Test case 3 failed"
    
    print("All test cases passed")

# Run the test function
test_first_order_linear()

# Plot the first-order linear system response
t_values = np.linspace(0, 10, 100)
y_values = first_order_linear(0, 1, 1, t_values)

plt.plot(t_values, y_values)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('First-Order Linear System')
plt.grid(True)
plt.show()
