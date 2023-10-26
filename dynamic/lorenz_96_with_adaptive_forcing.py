# Lorenz-96 Model with adaptive forcing
def lorenz_96_adaptive(Y, t, F, omega):
    N = len(Y)
    dYdt = np.zeros(N)
    for i in range(N):
        dYdt[i] = -Y[i-1] * (Y[i-2] - Y[(i+1) % N]) - Y[i] + F * (1 + np.sin(omega * t))
    return dYdt

# Test function for Lorenz-96 with adaptive forcing
def test_lorenz_96_adaptive():
    # Parameters
    F = 8.0
    omega = 0.1
    
    # Initial conditions
    N = 10  # Number of variables
    Y0 = np.random.rand(N)
    
    # Time vector
    t = np.linspace(0, 10, 1000)
    
    # Solve the differential equations
    sol = odeint(lorenz_96_adaptive, Y0, t, args=(F, omega))
    
    # Compute MSE between the first and second state variables
    mse_01 = mean_squared_error(sol[:, 0], sol[:, 1])
    
    # Assert that the MSE is within a certain range to ensure non-trivial behavior
    assert 0.1 < mse_01 < 100, f"MSE out of range: {mse_01}"
    
    return sol, t, mse_01

# Run the test function
sol, t, mse_01 = test_lorenz_96_adaptive()

# Plotting the attractor
plt.figure()
plt.plot(t, sol[:, 0], label='X0')
plt.plot(t, sol[:, 1], label='X1')
plt.title(f'Lorenz-96 Model with Adaptive Forcing\nMSE between X0 and X1: {mse_01:.4f}')
plt.xlabel('Time')
plt.ylabel('State Variables')
plt.legend()
plt.show()

# Print MSE to confirm the plot is sufficiently interesting
print(f"MSE between X0 and X1: {mse_01}")
