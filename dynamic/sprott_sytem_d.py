# Implementing the Sprott System D
# Reference: Sprott, J. C. (1994). Some simple chaotic flows. Physical Review E, 50(2), R647.

def sprott_d(y, t):
    """
    Differential equations for the Sprott System D.
    """
    x, y, z = y
    dxdt = -y
    dydt = x + y * z
    dzdt = 1 - y**2
    
    return [dxdt, dydt, dzdt]

def test_sprott_d():
    """
    Test function for Sprott System D.
    """
    # Initial conditions
    y0 = [0, 2, 0]
    t = np.linspace(0, 1, 1000)
    
    # Solve the system of equations
    solution = odeint(sprott_d, y0, t)
    
    # Validate the system has evolved (i.e., state variables shouldn't remain static).
    assert not np.allclose(solution[0, :], solution[-1, :]), "Test failed: The system did not evolve."

# Running the test
test_sprott_d()

# If test passes, we plot
# Initial conditions
y0 = [0, 2, 0]
t = np.linspace(0, 100, 10000)

# Solve the system of equations
solution = odeint(sprott_d, y0, t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(solution[:, 0], solution[:, 1])
plt.title("Sprott System D")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Compute and print a metric (MSE between first and last point) to confirm plot quality
mse_plot_quality = mean_squared_error(solution[0, :], solution[-1, :])
print(f"MSE between first and last point: {mse_plot_quality}")
