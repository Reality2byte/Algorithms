# Implementing the SIR Model with Birth and Death (Susceptible-Infected-Recovered)
# Equations:
# dS/dt = birth - beta * S * I - death * S
# dI/dt = beta * S * I - gamma * I - death * I
# dR/dt = gamma * I - death * R
def sir_birth_death(Y, t, beta, gamma, birth, death):
    S, I, R = Y
    dSdt = birth - beta * S * I - death * S
    dIdt = beta * S * I - gamma * I - death * I
    dRdt = gamma * I - death * R
    return [dSdt, dIdt, dRdt]

# Test function for SIR Model with Birth and Death
def test_sir_birth_death():
    # Parameters
    beta, gamma = 0.3, 0.1  # infection rate and recovery rate
    birth, death = 0.01, 0.01  # birth and death rates
    initial_conditions = [0.99, 0.01, 0]  # initial fractions of S, I, R
    t = np.linspace(0, 160, 5000)
    
    # Integrate the equations
    solution = odeint(sir_birth_death, initial_conditions, t, args=(beta, gamma, birth, death))
    
    # Plot the results
    plt.figure()
    plt.title("SIR Model with Birth and Death")
    plt.xlabel("Time")
    plt.ylabel("Fractions of Populations")
    plt.plot(t, solution[:, 0], label='S (Susceptible)')
    plt.plot(t, solution[:, 1], label='I (Infected)')
    plt.plot(t, solution[:, 2], label='R (Recovered)')
    plt.legend()
    plt.show()

    # Check if the system produces non-trivial dynamics (i.e., not converging to a single point)
    assert np.std(solution[-1000:, 0]) > 0.001
    assert np.std(solution[-1000:, 1]) > 0.001
    assert np.std(solution[-1000:, 2]) > 0.001

    print("SIR Model with Birth and Death Test Passed!")

# Run the test
test_sir_birth_death()
