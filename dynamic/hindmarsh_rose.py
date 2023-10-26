def hindmarsh_rose(Y, t, a, b, c, d, r, s, x_r, I):
    """
    Hindmarsh-Rose equations
    """
    x, y, z = Y
    dxdt = y - a * x**3 + b * x**2 - z + I
    dydt = c - d * x**2 - y
    dzdt = r * (s * (x - x_r) - z)
    return [dxdt, dydt, dzdt]

def plot_hindmarsh_rose(a=1.0, b=3.0, c=1.0, d=5.0, r=0.006, s=4.0, x_r=-1.6, I=2.0, time_steps=10000, time_end=300):
    """
    Plot the Hindmarsh-Rose system
    """
    # Initial conditions
    initial_conditions = [-1, -1, 1]
    
    # Time grid
    t = np.linspace(0, time_end, time_steps)
    
    # Solve the differential equations
    sol = odeint(hindmarsh_rose, initial_conditions, t, args=(a, b, c, d, r, s, x_r, I))
    
    # Plot the results
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, sol[:, 0], label='x(t)')
    plt.title('Hindmarsh-Rose System')
    plt.xlabel('Time')
    plt.ylabel('x(t)')
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(t, sol[:, 1], label='y(t)', color='orange')
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(t, sol[:, 2], label='z(t)', color='green')
    plt.xlabel('Time')
    plt.ylabel('z(t)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def test_hindmarsh_rose():
    """
    Test the Hindmarsh-Rose system by integrating it for a short time
    and checking if the output makes sense.
    """
    # Initial conditions
    initial_conditions = [-1, -1, 1]
    
    # Time grid
    t = np.linspace(0, 1, 10)
    
    # Solve the differential equations with parameters
    sol = odeint(hindmarsh_rose, initial_conditions, t, args=(1.0, 3.0, 1.0, 5.0, 0.006, 4.0, -1.6, 2.0))
    
    # Check if the output is a NumPy array with the correct shape
    assert isinstance(sol, np.ndarray), "Output should be a NumPy array"
    assert sol.shape == (10, 3), "Output shape should be (10, 3)"
    
    # Print the first few values of the solution
    print("Test passed. First few values of the solution:")
    print(sol[:3])

# Run the test function
test_hindmarsh_rose()

# Plot the Hindmarsh-Rose system
plot_hindmarsh_rose()
