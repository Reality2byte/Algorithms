# Implementing and testing the Rayleigh Oscillator
def rayleigh_oscillator(state, t, alpha, omega):
    """
    Rayleigh Oscillator Differential Equations
    """
    x, v = state
    dxdt = v
    dvdt = -omega**2 * x - alpha * v * (1 - x**2)
    return [dxdt, dvdt]

def test_rayleigh_oscillator():
    """
    Test function for Rayleigh Oscillator
    """
    # Define the initial conditions and parameters
    initial_state = [1.0, 0.0]
    t = np.linspace(0, 100, 1000)
    alpha, omega = 0.1, 1.0
    
    # Integrate the Rayleigh Oscillator equations on the time grid t
    solution = odeint(rayleigh_oscillator, initial_state, t, args=(alpha, omega))
    
    # Print output for verification (first 5 entries)
    print("First 5 entries of Rayleigh Oscillator:")
    print(solution[:5])
    
    # Plot
    plt.figure()
    plt.plot(t, solution[:, 0], label='x (Position)')
    plt.plot(t, solution[:, 1], label='v (Velocity)')
    plt.legend()
    plt.title('Rayleigh Oscillator')
    plt.xlabel('Time')
    plt.ylabel('State Variables')
    plt.show()

# Run the test to make sure the dynamic system is producing the expected outputs
test_rayleigh_oscillator()
