# Further adjust parameters and initial conditions to stabilize the system's behavior
def test_four_wing_attractor_stabilized():
    # Further adjusted parameters for the system
    a = 0.1
    b = 0.01
    c = 0.1
    d = 0.1
    e = 0.1

    # Further adjusted initial conditions [x, y, z]
    Y0 = [0.1, 0.1, 0.1]

    # Time grid for integration
    t = np.linspace(0, 100, 10000)

    # Solve the ODE system
    solution = odeint(four_wing_attractor, Y0, t, args=(a, b, c, d, e))

    # Separate the solution into x, y, z
    x, y, z = solution[:, 0], solution[:, 1], solution[:, 2]

    # Compute metric for 'interestingness' and 'beauty' (here, we use the range of z-values as a simple metric)
    metric = np.max(z) - np.min(z)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_title("Four-Wing Chaotic Attractor (Stabilized)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

    # Check if the metric meets the criteria for 'interesting and beautiful' (here, arbitrarily chosen as 1)
    assert metric > 1, f"Metric value is {metric}, expected > 1"

    print(f"Test passed. Metric value: {metric}")

# Run the test function with further adjusted parameters
test_four_wing_attractor_stabilized()
