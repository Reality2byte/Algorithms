# Implementing the Lorenz 84 Model
# The Lorenz 84 model is a simplified model for atmospheric dynamics, and it is a system of 
# three ordinary differential equations given by:
#
# dx/dt = -yx - zx + F
# dy/dt = xy - by - dz
# dz/dt = xz + dy - c*z

def lorenz_84(Y, t, F, b, c):
    x, y, z = Y
    dxdt = -y * x - z * x + F
    dydt = x * y - b * y - z
    dzdt = x * z + y - c * z
    return [dxdt, dydt, dzdt]

# Parameters
F = 1.0
b = 1.0
c = 1.0

# Initial conditions
initial_conditions = [0.1, 0.1, 0.1]

# Time grid for integration
t = np.linspace(0, 100, 10000)

# Integrate the equations
solution = odeint(lorenz_84, initial_conditions, t, args=(F, b, c))

# Plotting
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, solution[:, 0], label="x(t)")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, solution[:, 1], label="y(t)")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, solution[:, 2], label="z(t)")
plt.xlabel("Time")
plt.ylabel("z(t)")
plt.legend()

plt.tight_layout()
plt.show()

# Test function to verify the system
def test_lorenz_84():
    # Integrate for a short time to get the next state
    t_test = np.linspace(0, 1, 10)
    test_solution = odeint(lorenz_84, [0.1, 0.1, 0.1], t_test, args=(F, b, c))
    
    # Check if the system is not in a fixed point by making sure the state variables are changing
    dx = test_solution[-1, 0] - test_solution[0, 0]
    dy = test_solution[-1, 1] - test_solution[0, 1]
    dz = test_solution[-1, 2] - test_solution[0, 2]
    
    assert dx != 0 and dy != 0 and dz != 0, "The system is in a fixed point."
    
    print("Lorenz 84 test passed.")

# Run the test
test_lorenz_84()
