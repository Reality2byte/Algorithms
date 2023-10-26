from scipy.integrate import odeint

# Lorenz 84 with Seasonal Forcing
def lorenz_84_seasonal(Y, t, alpha=0.25, beta=4.0, F=8.0, G=1.0, epsilon=0.4):
    """Compute the right-hand side of Lorenz 84 system with seasonal forcing.
    
    Parameters:
        Y (array): Array of [x, y, z] values
        t (float): Time
        alpha, beta, F, G, epsilon (float): Parameters of the system
    
    Returns:
        array: Derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = Y
    dx_dt = -alpha*x + y*y - beta*x*z + F + epsilon*np.cos(np.pi * t / 5)
    dy_dt = x*y - y - x*z + G
    dz_dt = beta*x*y + x - z
    return [dx_dt, dy_dt, dz_dt]

# Test function for Lorenz 84 with Seasonal Forcing
def test_lorenz_84_seasonal():
    # Time grid for integration
    t = np.linspace(0, 2, 100)
    
    # Initial condition
    Y0 = [1.0, 1.0, 1.0]
    
    # Parameters
    alpha, beta, F, G, epsilon = 0.25, 4.0, 8.0, 1.0, 0.4
    
    # Integrate the ODEs
    sol = odeint(lorenz_84_seasonal, Y0, t, args=(alpha, beta, F, G, epsilon))
    
    # Check if the solution seems reasonable
    assert np.all(np.abs(sol) < 100), "Test failed! Solution values are out of expected range."
    print("Test passed!")

# Run the test
test_lorenz_84_seasonal()

# Generate and plot Lorenz 84 with Seasonal Forcing
# Time grid for integration
t = np.linspace(0, 100, 10000)

# Initial condition
Y0 = [1.0, 1.0, 1.0]

# Parameters
alpha, beta, F, G, epsilon = 0.25, 4.0, 8.0, 1.0, 0.4

# Integrate the ODEs
sol = odeint(lorenz_84_seasonal, Y0, t, args=(alpha, beta, F, G, epsilon))
x_vals, y_vals, z_vals = sol[:, 0], sol[:, 1], sol[:, 2]

# Calculate metric for plot's interestingness and beauty (standard deviation of the points)
metric = np.std(x_vals) + np.std(y_vals) + np.std(z_vals)

# Plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_vals, y_vals, z_vals, c=t, cmap='viridis', s=0.5)
ax.set_title(f"Lorenz 84 with Seasonal Forcing\nMetric: {metric:.4f}")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
