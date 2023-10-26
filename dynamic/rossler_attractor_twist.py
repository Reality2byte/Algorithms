from scipy.integrate import odeint

def rossler_twist(Y, t, a, b, c, d):
    """
    Implement the Rössler Attractor with a Twist, a continuous-time dynamical system.
    
    Parameters:
    Y (list): List containing the current x, y, and z values
    t (float): Current time (unused, required by odeint)
    a, b, c, d (float): Parameters in the Rössler equations
    
    Returns:
    list: List containing dx/dt, dy/dt, and dz/dt
    """
    x, y, z = Y
    dxdt = -y - z + d * x * y
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

def test_rossler_twist():
    """
    Test the Rössler Attractor with a Twist function to ensure it's working as expected.
    """
    a, b, c, d = 0.2, 0.2, 5.7, 0.1
    Y0 = [1.0, 1.0, 1.0]
    t = np.linspace(0, 1, 10)
    Y = odeint(rossler_twist, Y0, t, args=(a, b, c, d))
    
    assert Y.shape == (10, 3), "Shape of output should be (10, 3)"
    
    print("Rössler Attractor with a Twist test passed.")

# Run the test function
test_rossler_twist()

# Plotting
a, b, c, d = 0.2, 0.2, 5.7, 0.1
Y0 = [1.0, 1.0, 1.0]
t = np.linspace(0, 100, 10000)
Y = odeint(rossler_twist, Y0, t, args=(a, b, c, d))

plt.figure(figsize=(10, 8))
plt.plot(Y[:, 0], Y[:, 2])
plt.title("Rössler Attractor with a Twist")
plt.xlabel("x")
plt.ylabel("z")
plt.show()
