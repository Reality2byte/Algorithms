# Extending the Quintuple system to a Sextuple system by adding the Lotka-Volterra equations
def sextuple_hybrid_system_2(t, Y, harmonic_omega, van_der_pol_mu, duffing_alpha, duffing_beta, duffing_delta, duffing_gamma, duffing_omega, pendulum_g, pendulum_l, logistic_r, lotka_alpha, lotka_beta, lotka_delta, lotka_gamma):
    # Unpack variables
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = Y[:12]
    
    # Harmonic Oscillator dynamics
    dx1dt = y1
    dy1dt = -harmonic_omega ** 2 * x1

    # Van der Pol Oscillator
    dx2dt = y2
    dy2dt = van_der_pol_mu * (1 - x2 ** 2) * y2 - x2
    
    # Duffing Oscillator
    dx3dt = y3
    dy3dt = duffing_alpha * x3 - duffing_beta * x3 ** 3 - duffing_delta * y3 + duffing_gamma * np.cos(duffing_omega * t)

    # Simple Pendulum
    dx4dt = y4
    dy4dt = -(pendulum_g / pendulum_l) * np.sin(x4)
    
    # Logistic Map (Discrete, but approximated)
    dx5dt = logistic_r * x5 * (1 - x5)
    dy5dt = 0  # Not used, but needed for consistency
    
    # Lotka-Volterra
    dx6dt = lotka_alpha * x6 - lotka_beta * x6 * y6
    dy6dt = lotka_delta * x6 * y6 - lotka_gamma * y6
    
    # Mixing all dynamics
    dx7dt = dx1dt + dx2dt + dx3dt + dx4dt + dx5dt + dx6dt
    dy7dt = dy1dt + dy2dt + dy3dt + dy4dt + dy5dt + dy6dt
    
    return [dx1dt, dy1dt, dx2dt, dy2dt, dx3dt, dy3dt, dx4dt, dy4dt, dx5dt, dy5dt, dx6dt, dy6dt, dx7dt, dy7dt]

# Initial conditions and parameters
initial_conditions = [0.1]*14  # Initial conditions for all variables

# Parameters for Lotka-Volterra
lotka_alpha, lotka_beta, lotka_delta, lotka_gamma = 0.1, 0.02, 0.01, 0.1

# Time span
t_span = (0, 50)
t_eval = np.linspace(0, 50, 10000)

# Integrate the ODEs
sol = solve_ivp(
    sextuple_hybrid_system_2,
    t_span,
    initial_conditions,
    args=(harmonic_omega, van_der_pol_mu, duffing_alpha, duffing_beta, duffing_delta, duffing_gamma, duffing_omega, pendulum_g, pendulum_l, logistic_r, lotka_alpha, lotka_beta, lotka_delta, lotka_gamma),
    t_eval=t_eval,
)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[12], sol.y[13], sol.y[0])
ax.set_title('Sextuple Hybrid Dynamic System 2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
