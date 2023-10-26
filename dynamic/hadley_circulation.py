# Hadley Circulation Model
def hadley_circulation(state, t):
    """
    Hadley Circulation Model equations
    """
    x, y, z = state
    F, G, H, alpha, beta, delta = 8, 1, 8, 0.25, 4, 1  # Parameters
    
    dx = -y**2 - z**2 - alpha*x + alpha*F
    dy = x*y - beta*x*z - y + G
    dz = beta*x*y + x*z - z
    
    return [dx, dy, dz]

# Initial state [x, y, z]
initial_state = [0.1, 0, 0]

# Time grid for integration
t = np.linspace(0, 100, 10000)

# Integrate the Hadley Circulation equations over the time grid t
trajectory = odeint(hadley_circulation, initial_state, t)

# Plotting the Hadley Circulation Model
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], lw=0.5)
ax.set_title("Hadley Circulation Model")
plt.show()
