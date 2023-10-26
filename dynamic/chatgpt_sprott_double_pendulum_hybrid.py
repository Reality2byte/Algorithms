from scipy.integrate import solve_ivp

# Define the Sprott-Double Pendulum Hybrid System equations
def sprott_double_pendulum_hybrid(t, Y, alpha, l):
    x, y, z, x1, y1, x2, y2, theta, omega = Y
    px = x1 - x2
    py = y1 - y2

    # Mixing Sprott's Chaotic Jerk and Double Pendulum dynamics
    dxdt = y
    dydt = z
    dzdt = -x - 2 * y - z + alpha * x ** 3 + l * omega ** 2

    dx1dt = px
    dy1dt = py
    dx2dt = px + l * omega * np.cos(theta)
    dy2dt = py + l * omega * np.sin(theta)
    dthetadt = omega
    domegadt = -l * omega ** 2 * np.sin(2 * theta) / 2

    return [dxdt, dydt, dzdt, dx1dt, dy1dt, dx2dt, dy2dt, dthetadt, domegadt]

# Initial conditions and parameters
initial_conditions = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4]
alpha = 0.1  # Sprott's Chaotic Jerk parameter
l = 1.0  # Double Pendulum length
t_span = (0, 50)
t_eval = np.linspace(0, 50, 10000)

# Integrate the ODEs
sol = solve_ivp(
    sprott_double_pendulum_hybrid, t_span, initial_conditions, args=(alpha, l), t_eval=t_eval
)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_title('Sprott-Double Pendulum Hybrid System')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# Compute the fractal dimension for this new plot
H, xedges, yedges = np.histogram2d(sol.y[0], sol.y[1], bins=50)
H = H.T
fractal_dim = fractal_dimension(H)
fractal_dim
