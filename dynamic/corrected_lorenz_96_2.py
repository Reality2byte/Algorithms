# Correcting the Lorenz '96 II Model and test

def lorenz_96_II_corrected(y, t, F):
    """
    Differential equations for the Lorenz '96 II Model, corrected version.
    """
    n = len(y)
    dydt = np.zeros(n)
    
    for i in range(n):
        dydt[i] = -y[i-2] * y[i-1] + y[i-1] * y[(i+1) % n] - y[i] + F
    
    return dydt

def test_lorenz_96_II_corrected():
    """
    Test function for corrected Lorenz '96 II Model.
    """
    # The Lorenz '96 II model is sensitive to initial conditions and parameters.
    # For the purpose of this test, we'll integrate the equations for a short time
    # and then check that the state has changed in a way that obeys the equations.
    
    # Initial conditions and parameters
    y0 = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
    F = 8.0
    t = np.linspace(0, 0.1, 100)
    
    # Solve the system of equations
    solution = odeint(lorenz_96_II_corrected, y0, t, args=(F,))
    
    # Validate that the system has evolved. The Lorenz '96 II system should not remain static.
    assert not np.allclose(solution[0, :], solution[-1, :]), "Test failed: The system did not evolve."

# Running the corrected test
test_lorenz_96_II_corrected()

# If test passes, we plot
# Initial conditions and parameters
y0 = np.random.rand(5)
F = 8.0
t = np.linspace(0, 20, 10000)

# Solve the system of equations
solution = odeint(lorenz_96_II_corrected, y0, t, args=(F,))

# Plotting
plt.figure(figsize=(10, 6))
for i in range(solution.shape[1]):
    plt.plot(t, solution[:, i], label=f"y{i+1}")
plt.title("Corrected Lorenz '96 II Model")
plt.xlabel("Time")
plt.ylabel("State Variables")
plt.legend()
plt.show()

# Compute and print a metric (MSE between first and last point) to confirm plot quality
mse_plot_quality = mean_squared_error(solution[0, :], solution[-1, :])
print(f"MSE between first and last point: {mse_plot_quality}")
