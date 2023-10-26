import numpy as np
import matplotlib.pyplot as plt

def exponential_growth(y0, r, t):
    """
    Calculate the exponential growth.
    
    Parameters:
    y0 (float): initial value
    r (float): rate of growth
    t (float): time
    
    Returns:
    float: value at time t
    """
    return y0 * np.exp(r * t)

def test_exponential_growth():
    """
    Test the exponential_growth function.
    """
    # Test case 1: y0=1, r=1, t=0 should return 1
    assert np.isclose(exponential_growth(1, 1, 0), 1), "Test case 1 failed"
    
    # Test case 2: y0=2, r=0, t=10 should return 2
    assert np.isclose(exponential_growth(2, 0, 10), 2), "Test case 2 failed"
    
    # Test case 3: y0=1, r=1, t=1 should return e
    assert np.isclose(exponential_growth(1, 1, 1), np.exp(1)), "Test case 3 failed"
    
    print("All test cases passed")

# Run the test function
test_exponential_growth()

# Plot the exponential growth
t_values = np.linspace(0, 2, 100)
y_values = exponential_growth(1, 1, t_values)

plt.plot(t_values, y_values)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Exponential Growth')
plt.grid(True)
plt.show()
