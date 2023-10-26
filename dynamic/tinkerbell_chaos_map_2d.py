import numpy as np
import matplotlib.pyplot as plt

# Tinkerbell Chaos Map 2D
def tinkerbell_chaos_2d(x, y, a=0.9, b=-0.6013, c=2.0, d=0.5):
    """Computes the next (x, y) point in the Tinkerbell Chaos 2D Map.
    
    Parameters:
        x, y (float): Current point coordinates
        a, b, c, d (float): Parameters of the map
        
    Returns:
        tuple: The next point (x', y') in the map
    """
    x_next = x*x - y*y + a*x + b*y
    y_next = 2*x*y + c*x + d*y
    return x_next, y_next

# Test function for the Tinkerbell Chaos 2D Map
def test_tinkerbell_chaos_2d():
    x, y = 0.1, 0.1  # Initial conditions
    a, b, c, d = 0.9, -0.6013, 2.0, 0.5  # Parameters
    
    # Generate some points
    points = []
    for _ in range(100):
        points.append((x, y))
        x, y = tinkerbell_chaos_2d(x, y, a, b, c, d)
    
    # Check if the points seem reasonable (i.e., within the expected range)
    assert all(-5 <= x <= 5 and -5 <= y <= 5 for x, y in points), "Test failed! Points are out of expected range."
    print("Test passed!")

# Run the test
test_tinkerbell_chaos_2d()

# Generate and plot the Tinkerbell Chaos 2D
n_points = 10000
x, y = 0.1, 0.1  # Initial conditions
a, b, c, d = 0.9, -0.6013, 2.0, 0.5  # Parameters

x_vals, y_vals = [], []
for _ in range(n_points):
    x_vals.append(x)
    y_vals.append(y)
    x, y = tinkerbell_chaos_2d(x, y, a, b, c, d)

# Calculate metric for plot's interestingness and beauty (standard deviation of the points)
metric = np.std(x_vals) + np.std(y_vals)

# Plotting
plt.figure(figsize=(10, 10))
plt.scatter(x_vals, y_vals, c='blue', s=0.5)
plt.title(f"Tinkerbell Chaos 2D Map\nMetric: {metric:.4f}")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
