def ikeda_map(u, x0, y0, n):
    """
    Implement the Ikeda map, a discrete-time dynamical system.
    
    Parameters:
    u (float): Parameter u in the Ikeda map equation
    x0 (float): Initial value of x
    y0 (float): Initial value of y
    n (int): Number of iterations
    
    Returns:
    np.ndarray: Array containing the x and y values
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        t = 0.4 - 6 / (1 + x_values[-1]**2 + y_values[-1]**2)
        x_new = 1 + u * (x_values[-1] * np.cos(t) - y_values[-1] * np.sin(t))
        y_new = u * (x_values[-1] * np.sin(t) + y_values[-1] * np.cos(t))
        
        x_values.append(x_new)
        y_values.append(y_new)
        
    return np.array(x_values), np.array(y_values)

def test_ikeda_map():
    """
    Test the Ikeda map function to ensure it's working as expected.
    """
    u = 0.9
    x0, y0 = 0, 0
    n = 10
    x_values, y_values = ikeda_map(u, x0, y0, n)
    
    assert len(x_values) == n + 1, "Length of x_values should be n + 1"
    assert len(y_values) == n + 1, "Length of y_values should be n + 1"
    assert np.isclose(x_values[0], x0), "First element of x_values should be x0"
    assert np.isclose(y_values[0], y0), "First element of y_values should be y0"
    
    print("Ikeda map test passed.")

# Run the test function
test_ikeda_map()

# Plotting
u = 0.9
x0, y0 = 0, 0
n = 1000
x_values, y_values = ikeda_map(u, x0, y0, n)

plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, c='blue', s=1)
plt.title("Ikeda Map")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
