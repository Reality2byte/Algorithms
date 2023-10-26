# Define Liu Chen System equations
def liu_chen(y, t, a, b, c):
    x, y, z = y
    dxdt = a * (y - x)
    dydt = (c - a) * x - x * z + c * y
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]

# Test the Liu Chen System
def test_liu_chen():
    # Parameters
    a, b, c = 40, 2, 28
    initial_conditions = [0.1, 0, 0.1]
    t = np.linspace(0, 100, 10000)
    
    # Numerical integration
    solution = odeint(liu_chen, initial_conditions, t, args=(a, b, c))
    
    # Plotting
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.plot(solution[:, 0], solution[:, 1], solution[:, 2])
    ax.set_title('Liu Chen Attractor')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()
    
    # Metric for "interest" and "beauty": Fractal Dimension
    # A simple proxy is to calculate the range of x, y, and z
    x_range = np.ptp(solution[:, 0])
    y_range = np.ptp(solution[:, 1])
    z_range = np.ptp(solution[:, 2])
    
    # Simple metric: sum of the ranges (larger values imply more "interesting" dynamics)
    metric = x_range + y_range + z_range
    return metric

# Run the test
metric_value = test_liu_chen()
print(f"Interest and Beauty Metric: {metric_value}")
