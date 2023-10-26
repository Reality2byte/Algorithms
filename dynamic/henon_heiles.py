# Implementing the Hénon-Heiles system
def henon_heiles_system(state, t, a, b):
    x, y, px, py = state
    dxdt = px
    dydt = py
    dpxdt = -x - 2 * a * x * y
    dpydt = -y - a * (x ** 2 - b)
    return [dxdt, dydt, dpxdt, dpydt]

# Test function for Hénon-Heiles system
def test_henon_heiles_system():
    a, b = 1.0, 1.0
    initial_state = [0.1, 0.0, 0.5, 0.5]
    t = np.linspace(0, 100, 10000)
    
    # Solving the system of ODEs
    solution = odeint(henon_heiles_system, initial_state, t, args=(a, b))
    
    # Plotting the system
    plt.figure()
    plt.plot(solution[:, 0], solution[:, 1])
    plt.title("Hénon-Heiles system")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    # Test condition: check if the system is non-trivial (not constant)
    assert not np.allclose(solution[0, :], solution[-1, :]), "The system seems to be trivial."
    print("Hénon-Heiles system test passed.")

# Running the test
test_henon_heiles_system()
