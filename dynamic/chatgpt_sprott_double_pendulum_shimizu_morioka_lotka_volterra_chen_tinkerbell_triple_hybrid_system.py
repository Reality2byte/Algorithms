# Define the triple hybrid system equations
def triple_hybrid_system(t, Y, sprott_alpha, double_pendulum_l, shimizu_a, shimizu_b, lotka_alpha, lotka_beta, lotka_delta, lotka_gamma, chen_a, chen_b, chen_c, tinkerbell_d, tinkerbell_e, tinkerbell_f):
    # Unpack variables
    x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = Y
    
    # Sprott-Double Pendulum dynamics
    dx1dt = y1
    dy1dt = z1
    dz1dt = -x1 - 2 * y1 - z1 + sprott_alpha * x1 ** 3 + double_pendulum_l * y2 ** 2

    # Shimizu-Morioka-Lotka-Volterra dynamics
    dx2dt = y2 + lotka_alpha * x3 - lotka_beta * x3 * y3
    dy2dt = -x2 + shimizu_a * x2 - y2 * z2 + shimizu_b * x3 * y3 - lotka_gamma * y3
    dz2dt = -shimizu_b * z2 + x2 * y2
    
    # Chen-Tinkerbell dynamics
    dx3dt = chen_a * (y3 - x3) + tinkerbell_d * (x4 ** 2 - y4 ** 2)
    dy3dt = (chen_c - chen_a) * x3 - x3 * z3 + chen_c * y3 + tinkerbell_e * (2 * x4 * y4)
    dz3dt = x3 * y3 - chen_b * z3 + tinkerbell_f * x4 + tinkerbell_f * y4

    # Mixing all dynamics
    dx4dt = dx1dt + dx2dt + dx3dt
    dy4dt = dy1dt + dy2dt + dy3dt
    dz4dt = dz1dt + dz2dt + dz3dt
    
    return [dx1dt, dy1dt, dz1dt, dx2dt, dy2dt, dz2dt, dx3dt, dy3dt, dz3dt, dx4dt, dy4dt, dz4dt]

# Initial conditions and parameters
initial_conditions = [0.1]*12  # Initial conditions for all variables

# Parameters for all three original systems
sprott_alpha = 0.1
double_pendulum_l = 1.0
shimizu_a, shimizu_b = 0.1, 0.1
lotka_alpha, lotka_beta, lotka_delta, lotka_gamma = 0.1, 0.02, 0.01, 0.1
chen_a, chen_b, chen_c = 36.0, 20.0, 16.0
tinkerbell_d, tinkerbell_e, tinkerbell_f = 0.9, 0.9, 0.3

# Time span
t_span = (0, 50)
t_eval = np.linspace(0, 50, 10000)

# Integrate the ODEs
sol = solve_ivp(
    triple_hybrid_system,
    t_span,
    initial_conditions,
    args=(sprott_alpha, double_pendulum_l, shimizu_a, shimizu_b, lotka_alpha, lotka_beta, lotka_delta, lotka_gamma, chen_a, chen_b, chen_c, tinkerbell_d, tinkerbell_e, tinkerbell_f),
    t_eval=t_eval,
)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_title('Triple Hybrid System')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# Compute the fractal dimension for this new plot
H, xedges, yedges = np.histogram2d(sol.y[0], sol.y[1], bins=50)
H = H.T
fractal_dim = fractal_dimension(H)
fractal_dim
