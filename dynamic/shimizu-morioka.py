# Adjust Shimizu-Morioka system parameters and re-run the test
def test_shimizu_morioka_v2():
    # Parameters
    a = 0.75
    b = 0.2
    initial_conditions = [0.1, 0.1, 0.1]
    t = np.linspace(0, 50, 10000)
    
    # Simulate the system
    solution = odeint(shimizu_morioka, initial_conditions, t, args=(a, b))
    
    # Plotting
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(solution[:, 0], solution[:, 1], solution[:, 2])
    ax.set_title('Shimizu-Morioka Attractor')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    
    # A metric to assess the plot: Standard Deviation of the X, Y, Z components
    std_x = np.std(solution[:, 0])
    std_y = np.std(solution[:, 1])
    std_z = np.std(solution[:, 2])
    
    # For an interesting and beautiful plot, we expect some variation in each component
    # Here, we check if standard deviation of each component is above a threshold
    threshold = 0.1
    if std_x > threshold and std_y > threshold and std_z > threshold:
        print(f"Test Passed: Standard Deviations - X: {std_x}, Y: {std_y}, Z: {std_z}")
    else:
        print("Test Failed")

# Run the test
test_shimizu_morioka_v2()
