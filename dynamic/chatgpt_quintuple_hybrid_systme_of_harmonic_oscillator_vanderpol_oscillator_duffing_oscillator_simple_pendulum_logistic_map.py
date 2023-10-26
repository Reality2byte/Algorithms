
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define a New Quintuple Hybrid Dynamic System using different base systems
def new_quintuple_hybrid_system_2(t, Y, harmonic_omega, van_der_pol_mu, duffing_alpha, duffing_beta, duffing_delta, duffing_gamma, duffing_omega, pendulum_g, pendulum_l, logistic_r):
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = Y[:10]
    dx1dt = y1
    dy1dt = -harmonic_omega ** 2 * x1
    dx2dt = y2
    dy2dt = van_der_pol_mu * (1 - x2 ** 2) * y2 - x2
    dx3dt = y3
    dy3dt = duffing_alpha * x3 - duffing_beta * x3 ** 3 - duffing_delta * y3 + duffing_gamma * np.cos(duffing_omega * t)
    dx4dt = y4
    dy4dt = -(pendulum_g / pendulum_l) * np.sin(x4)
    dx5dt = logistic_r * x5 * (1 - x5)
    dy5dt = 0
    dx6dt = dx1dt + dx2dt + dx3dt + dx4dt + dx5dt
    dy6dt = dy1dt + dy2dt + dy3dt + dy4dt + dy5dt
    return [dx1dt, dy1dt, dx2dt, dy2dt, dx3dt, dy3dt, dx4dt, dy4dt, dx5dt, dy5dt, dx6dt, dy6dt]

# Initial conditions and parameters
initial_conditions = [0.1]*12

# Parameters for all five original systems
harmonic_omega = 1.0
van_der_pol_mu = 1.0
duffing_alpha, duffing_beta, duffing_delta, duffing_gamma, duffing_omega = 1.0, 1.0, 0.3, 0.3, 1.2
pendulum_g, pendulum_l = 9.81, 1.0
logistic_r = 3.9

# Time span
t_span = (0, 50)
t_eval = np.linspace(0, 50, 10000)

# Integrate the ODEs
sol = solve_ivp(
    new_quintuple_hybrid_system_2,
    t_span,
    initial_conditions,
    args=(harmonic_omega, van_der_pol_mu, duffing_alpha, duffing_beta, duffing_delta, duffing_gamma, duffing_omega, pendulum_g, pendulum_l, logistic_r),
    t_eval=t_eval,
)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[10], sol.y[11], sol.y[0])
ax.set_title('New Quintuple Hybrid Dynamic System 2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
