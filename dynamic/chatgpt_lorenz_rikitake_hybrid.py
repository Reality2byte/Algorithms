# Define the Lorenz-Rikitake Hybrid System equations
def lorenz_rikitake_hybrid(Y, t, sigma, rho, beta, mu):
    x, y, z = Y
    # Mixing Lorenz '63 and Rikitake Dynamo dynamics
    dxdt = sigma * (y - x) - mu * x + y * z
    dydt = x * (rho - z) - y - mu * y + x * z
    dzdt = x * y - beta * z + 1 - x ** 2 - y ** 2
    
    return [dxdt, dydt, dzdt]

# Initial conditions and parameters
initial_conditions = [0.1, 0.1, 0.1]
sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0  # Lorenz '63 parameters
mu = 0.1  # Rikitake Dynamo parameter
t = np.linspace(0, 50, 10000)  # Time grid

# Integrate the ODEs
trajectory = odeint(lorenz_rikitake_hybrid, initial_conditions, t, args=(sigma, rho, beta, mu))

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2])
ax.set_title('Lorenz-Rikitake Hybrid System')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# Compute the fractal dimension for this new plot
H, xedges, yedges = np.histogram2d(trajectory[:, 0], trajectory[:, 1], bins=50)
H = H.T
fractal_dim = fractal_dimension(H)
fractal_dim
