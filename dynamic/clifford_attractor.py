def clifford_attractor(x, y, a, b, c, d):
    """
    Computes the next (x, y) point in the Clifford Attractor.
    Parameters:
        x, y : current coordinates
        a, b, c, d : parameters of the attractor
    Returns:
        new_x, new_y : new coordinates
    """
    new_x = np.sin(a * y) + c * np.cos(a * x)
    new_y = np.sin(b * x) + d * np.cos(b * y)
    
    return new_x, new_y

def test_clifford_attractor():
    """
    Test the Clifford Attractor function to ensure it is working as expected.
    """
    x, y = 0, 0
    a, b, c, d = 1.5, -1.8, 1.6, 0.9
    next_x, next_y = clifford_attractor(x, y, a, b, c, d)
    
    # These are expected outputs for given inputs, calculated manually
    expected_next_x = 1.6
    expected_next_y = 0.9
    
    assert np.isclose(next_x, expected_next_x), f"Expected {expected_next_x}, got {next_x}"
    assert np.isclose(next_y, expected_next_y), f"Expected {expected_next_y}, got {next_y}"

    print("Clifford Attractor test passed.")

# Run the test
test_clifford_attractor()

# Simulate the Clifford Attractor
n_points = 10000  # Number of points to generate
x, y = 0.1, 0.1  # Initial condition
a, b, c, d = 1.5, -1.8, 1.6, 0.9  # Parameters
x_vals, y_vals = [x], [y]

for _ in range(n_points):
    x, y = clifford_attractor(x, y, a, b, c, d)
    x_vals.append(x)
    y_vals.append(y)

# Plot the attractor
plt.figure(figsize=(10, 10))
plt.scatter(x_vals, y_vals, c=range(len(x_vals)), cmap='plasma', s=0.6)
plt.title("Clifford Attractor")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label='Iteration')
plt.show()

# Metric for plot's complexity: the number of unique points
unique_points = len(set(zip(x_vals, y_vals)))
print(f"Metric for plot's complexity: Number of unique points = {unique_points}")
