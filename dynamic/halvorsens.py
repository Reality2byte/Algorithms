# Implementing Halvorsen's Attractor
def halvorsens_attractor(t, y, a):
    x, y, z = y
    
    dx_dt = -a * x - 4 * y - 4 * z - y ** 2
    dy_dt = -a * y - 4 * z - 4 * x - z ** 2
    dz_dt = -a * z - 4 * x - 4 * y - x ** 2
    
    return [dx_dt, dy_dt, dz_dt]

# Test function to validate the implementation
def test_halvorsens_attractor():
    # Initial conditions
    y0 = [0.1, 0.0, 0.0]
    t_span = (0, 100)
    t_eval = np.linspace(t_span[0], t_span[1], 10000)
    
    # Parameter (a)
    a = 1.4
    
    # Solve the differential equations
    sol = odeint(halvorsens_attractor, y0, t_eval, args=(a,), tfirst=True)
    
    # Validate some basic properties, e.g., check if the solution diverges or converges
    # For a chaotic system like this, we expect the solution to not converge to a single point
    assert not np.allclose(sol[-1], sol[0])
    
    return sol

# Plotting function
def plot_halvorsens_attractor(sol):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2])
    ax.set_title("Halvorsen's Attractor")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

# Running the test
sol = test_halvorsens_attractor()
print("Test passed for Halvorsen's Attractor.")

# Plot the solution
plot_halvorsens_attractor(sol)
