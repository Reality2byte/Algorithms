import numpy as np
import matplotlib.pyplot as plt

def gumowski_mira(x, y, a, b):
    """
    Computes the next (x, y) point in the Gumowski-Mira attractor.
    Parameters:
        x, y : current coordinates
        a, b : parameters of the attractor
    Returns:
        new_x, new_y : new coordinates
    """
    def g(x):
        return a * x + 2 * (1 - a) * x**2 / (1 + x**2)
    
    new_x = y + g(x)
    new_y = -x + g(new_x)
    
    return new_x, new_y

def test_gumowski_mira():
    """
    Test the Gumowski-Mira function to ensure it is working as expected.
    """
    x, y = 0, 0
    a, b = 0.008, -0.7
    next_x, next_y = gumowski_mira(x, y, a, b)
    
    # These are expected outputs for given inputs, calculated manually
    expected_next_x = 0
    expected_next_y = 0
    
    assert np.isclose(next_x, expected_next_x), f"Expected {expected_next_x}, got {next_x}"
    assert np.isclose(next_y, expected_next_y), f"Expected {expected_next_y}, got {next_y}"

    print("Gumowski-Mira test passed.")

# Run the test
test_gumowski_mira()

# Simulate the Gumowski-Mira attractor
n_points = 10000  # Number of points to generate
x, y = 0.1, 0.1  # Initial condition
a, b = 0.008, -0.7  # Parameters
x_vals, y_vals = [x], [y]

for _ in range(n_points):
    x, y = gumowski_mira(x, y, a, b)
    x_vals.append(x)
    y_vals.append(y)

# Plot the attractor
plt.figure(figsize=(10, 10))
plt.scatter(x_vals, y_vals, c=range(len(x_vals)), cmap='viridis', s=0.6)
plt.title("Gumowski-Mira Attractor")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label='Iteration')
plt.show()

# Metric for plot's complexity: the number of unique points
# Note: This is a simple metric and may not capture all aspects of complexity and beauty.
unique_points = len(set(zip(x_vals, y_vals)))
print(f"Metric for plot's complexity: Number of unique points = {unique_points}")
