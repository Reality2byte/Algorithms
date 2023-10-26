import numpy as np
import matplotlib.pyplot as plt

def henon_map(a, b, x0, y0, n):
    """
    Implement the Henon map, a discrete-time dynamical system.
    
    Parameters:
    a (float): Parameter a in Henon map equation
    b (float): Parameter b in Henon map equation
    x0 (float): Initial value of x
    y0 (float): Initial value of y
    n (int): Number of iterations
    
    Returns:
    np.ndarray: Array containing the x and y values
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        x_new = 1 - a * x_values[-1]**2 + y_values[-1]
        y_new = b * x_values[-1]
        
        x_values.append(x_new)
        y_values.append(y_new)
        
    return np.array(x_values), np.array(y_values)

def test_henon_map():
    """
    Test the Henon map function to ensure it's working as expected.
    """
    a, b = 1.4, 0.3
    x0, y0 = 0, 0
    n = 10
    x_values, y_values = henon_map(a, b, x0, y0, n)
    
    assert len(x_values) == n + 1, "Length of x_values should be n + 1"
    assert len(y_values) == n + 1, "Length of y_values should be n + 1"
    assert np.isclose(x_values[0], x0), "First element of x_values should be x0"
    assert np.isclose(y_values[0], y0), "First element of y_values should be y0"
    
    print("Henon map test passed.")

# Run the test function
test_henon_map()

# Plotting
a, b = 1.4, 0.3
x0, y0 = 0, 0
n = 1000
x_values, y_values = henon_map(a, b, x0, y0, n)

plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, c='blue', s=1)
plt.title("Henon Map")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
