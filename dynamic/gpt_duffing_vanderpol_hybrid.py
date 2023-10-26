# Define the Duffing-Van der Pol Hybrid System equations
def duffing_vanderpol_hybrid(Y, t, delta, beta, omega, mu):
    x, y = Y
    dxdt = y
    # Mixing Duffing and Van der Pol dynamics
    dydt = x - x ** 3 - delta * y + beta * np.cos(omega * t) + mu * (1 - x ** 2) * y
    return [dxdt, dydt]

# Initial conditions and parameters
initial_conditions = [0.1, 0.1]
delta, beta, omega = 0.15, 0.3, 1.0  # Duffing parameters
mu = 2.0  # Van der Pol parameter
t = np.linspace(0, 100, 10000)  # Time grid

# Integrate the ODEs
trajectory = odeint(duffing_vanderpol_hybrid, initial_conditions, t, args=(delta, beta, omega, mu))

# Plotting
fig, ax = plt.subplots()
ax.plot(trajectory[:, 0], trajectory[:, 1])
ax.set_title('Duffing-Van der Pol Hybrid System')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()

# Compute the fractal dimension for this new plot
H, xedges, yedges = np.histogram2d(trajectory[:, 0], trajectory[:, 1], bins=50)
H = H.T
fractal_dim = fractal_dimension(H)
fractal_dim
