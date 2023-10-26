# Implementing the Rayleigh-Benard Convection System
# Equations:
# dx/dt = -a * x + a * y
# dy/dt = b * x - y - x * z
# dz/dt = -c * z + x * y
def rayleigh_benard_convection(Y, t, a, b, c):
    x, y, z = Y
    dxdt = -a * x + a * y
    dydt = b * x - y - x * z
    dzdt = -c * z + x * y
    return [dxdt, dydt, dzdt]

# Test function for Rayleigh-Benard Convection System
def test_rayleigh_benard_convection():
    # Parameters
    a, b, c = 0.5, 2.0, 4.0
    initial_conditions = [1.0, 1.0, 1.0]
    t = np.linspace(0, 50, 5000)
    
    # Integrate the equations
    solution = odeint(rayleigh_benard_convection, initial_conditions, t, args=(a, b, c))
    
    # Plot the results
    plt.figure()
    plt.title("Rayleigh-Benard Convection System")
    plt.xlabel("Time")
    plt.ylabel("State Variables")
    plt.plot(t, solution[:, 0], label='x')
    plt.plot(t, solution[:, 1], label='y')
    plt.plot(t, solution[:, 2], label='z')
    plt.legend()
    plt.show()

    # Check if the system produces non-trivial dynamics (i.e., not converging to a single point)
    assert np.std(solution[-1000:, 0]) > 0.1
    assert np.std(solution[-1000:, 1]) > 0.1
    assert np.std(solution[-1000:, 2]) > 0.1

    print("Rayleigh-Benard Convection Test Passed!")

# Run the test
test_rayleigh_benard_convection()
