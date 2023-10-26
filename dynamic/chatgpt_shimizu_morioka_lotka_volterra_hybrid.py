# Define the Shimizu-Morioka-Lotka-Volterra Hybrid System equations
def shimizu_morioka_lotka_volterra_hybrid(t, Y, a, b, alpha, beta, delta, gamma):
    x, y, z = Y
    # Mixing Shimizu-Morioka and Lotka-Volterra dynamics
    dxdt = y + alpha * x - beta * x * y
    dydt = -x + a * x - y * z + delta * x * y - gamma * y
    dzdt = -b * z + x * y
    
    return [dxdt, dydt, dzdt]

# Initial conditions and parameters
initial_conditions = [0.1, 0.1, 0.1]
a, b = 0.1, 0.1  # Shimizu-Morioka parameters
alpha, beta, delta, gamma = 0.1, 0.02, 0.01, 0.1  # Lotka-Volterra parameters
t_span = (0, 100)
t_eval = np.linspace(0, 100, 10000)

# Integrate the ODEs
sol = solve_ivp(
    shimizu_morioka_lotka_volterra_hybrid,
    t_span,
    initial_conditions,
    args=(a, b, alpha, beta, delta, gamma),
    t_eval=t_eval,
)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_title('Shimizu-Morioka-Lotka-Volterra Hybrid System')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# Compute the fractal dimension for this new plot
H, xedges, yedges = np.histogram2d(sol.y[0], sol.y[1], bins=50)
H = H.T
fractal_dim = fractal_dimension(H)
fractal_dim
