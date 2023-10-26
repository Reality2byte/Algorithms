import numpy as np
import matplotlib.pyplot as plt

def ikeda_time_delay(n, u, x0, y0):
    """
    Generate n points of the Ikeda Time Delay attractor.
    
    Parameters:
    n (int): Number of points to generate
    u (float): Parameter value
    x0, y0 (float): Initial conditions
    
    Returns:
    np.ndarray: x and y coordinates of the attractor
    """
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = x0, y0
    
    for i in range(n-1):
        t = 0.4 - 6 / (1 + x[i]**2 + y[i]**2)
        x[i+1] = 1 + u * (x[i] * np.cos(t) - y[i] * np.sin(t))
        y[i+1] = u * (x[i] * np.sin(t) + y[i] * np.cos(t))
        
    return x, y

def test_ikeda_time_delay():
    """
    Test the Ikeda Time Delay function by generating a sequence and checking the first few values.
    """
    n = 10
    u = 0.9
    x0, y0 = 0, 0
    x, y = ikeda_time_delay(n, u, x0, y0)
    
    assert np.isclose(x[0], 0, atol=1e-5), f"Expected x[0] = 0, got {x[0]}"
    assert np.isclose(y[0], 0, atol=1e-5), f"Expected y[0] = 0, got {y[0]}"
    
    print("Test passed.")

# Test the Ikeda Time Delay function
test_ikeda_time_delay()

# Generate the Ikeda Time Delay attractor
n = 10000
u = 0.9
x0, y0 = 0, 0
x, y = ikeda_time_delay(n, u, x0, y0)

# Plot the attractor
plt.figure(figsize=(10, 10))
plt.scatter(x, y, c=np.arange(n), cmap='viridis', s=1)
plt.title('Ikeda Time Delay Attractor')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Iteration')
plt.show()
