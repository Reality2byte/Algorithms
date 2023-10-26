import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the Nosé-Hoover Chain equations
def nose_hoover_chain(Y, t, Q1, Q2):
    x1, p1, x2, p2, z1, z2 = Y
    dx1dt = p1
    dp1dt = -x1 - (Q1 * p1 * z1)
    dx2dt = p2
    dp2dt = -x2 - (Q2 * p2 * z2)
    dz1dt = p1**2 - 1
    dz2dt = p2**2 - 1

    return [dx1dt, dp1dt, dx2dt, dp2dt, dz1dt, dz2dt]

# Time settings
Tmax = 100
N = 10000
t = np.linspace(0, Tmax, N)

# Parameters
Q1 = 1.0
Q2 = 1.0

# Initial conditions
Y0 = [0.0, 1.0, 0.0, 1.0, 0.0, 0.0]

# Solve the ODEs
sol = odeint(nose_hoover_chain, Y0, t, args=(Q1, Q2))

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(sol[:, 0], sol[:, 1])
plt.title('Phase Space of First Oscillator')
plt.xlabel('x1')
plt.ylabel('p1')

plt.subplot(2, 2, 2)
plt.plot(sol[:, 2], sol[:, 3])
plt.title('Phase Space of Second Oscillator')
plt.xlabel('x2')
plt.ylabel('p2')

plt.subplot(2, 2, 3)
plt.plot(t, sol[:, 4])
plt.title('z1 vs Time')
plt.xlabel('Time')
plt.ylabel('z1')

plt.subplot(2, 2, 4)
plt.plot(t, sol[:, 5])
plt.title('z2 vs Time')
plt.xlabel('Time')
plt.ylabel('z2')

plt.tight_layout()
plt.show()

# Define a test function to validate the results
def test_nose_hoover_chain():
    # Test initial conditions
    assert np.isclose(sol[0, :], Y0).all()

    # Test conservation of the "extended" Hamiltonian to some tolerance
    H_extended = sol[:, 1]**2 / 2 + sol[:, 0]**2 / 2 + sol[:, 3]**2 / 2 + sol[:, 2]**2 / 2 + \
                 Q1 * sol[:, 4] + Q2 * sol[:, 5]
    assert np.isclose(H_extended[0], H_extended[-1], atol=1e-2)

test_nose_hoover_chain()
print("Nosé-Hoover Chain test passed.")
