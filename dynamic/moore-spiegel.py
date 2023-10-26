# Step 1: Re-Implement the Moore-Spiegel attractor equations (no change)
# The equations remain the same

# Step 2: Re-Test function for Moore-Spiegel attractor (no change)
# The test remains the same

# Run the test function again
test_moore_spiegel()

# Step 3: Re-Plot the attractor with adjusted parameters and initial conditions
# Adjusted Parameters and initial conditions
initial_state = [0.1, 0, 0]
a, b, c, d = 0.4, 0.6, 0.5, 1.0
t = np.linspace(0, 100, 10000)

# Compute the attractor trajectory
trajectory = odeint(moore_spiegel, initial_state, t, args=(a, b, c, d))

# Re-Plotting
plt.figure(figsize=(10, 8))
plt.plot(trajectory[:,0], trajectory[:,2], 'b', linewidth=0.5)
plt.title("Moore-Spiegel Attractor")
plt.xlabel("x")
plt.ylabel("z")
plt.show()

# Step 4: Re-Compute a metric on the plot
# Use the standard deviation of x and z as a simple metric for "interestingness"
std_x = np.std(trajectory[:,0])
std_z = np.std(trajectory[:,2])
interestingness_metric = std_x * std_z

print(f"Interestingness Metric: {interestingness_metric}")
