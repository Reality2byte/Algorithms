# Next, let's implement the FitzHugh-Nagumo model, a simplified version of the Hodgkin-Huxley model for neuronal activity.
# The equations are:
# dv/dt = v - v^3/3 - w + I
# dw/dt = 0.08 * (v + 0.7 - 0.8 * w)
# It has one parameter I (external current) and two state variables v (membrane potential) and w (recovery variable).

def fitzhugh_nagumo_model(state, t, I):
    """
    Define the FitzHugh-Nagumo model.
    
    Parameters:
    - state: array, the state variables [v, w]
    - t: float, time
    - I: float, external current parameter of the model
    
    Returns:
    - derivatives: array, the derivatives [dv/dt, dw/dt]
    """
    v, w = state
    dv_dt = v - (v ** 3) / 3 - w + I
    dw_dt = 0.08 * (v + 0.7 - 0.8 * w)
    return [dv_dt, dw_dt]

def test_fitzhugh_nagumo_model():
    """
    Test the FitzHugh-Nagumo model by comparing numerical simulation with expected behavior.
    """
    I = 0.5
    initial_state = [-1.0, 1.0]
    t = np.linspace(0, 100, 1000)
    
    # Solve the differential equations numerically
    sol = odeint(fitzhugh_nagumo_model, initial_state, t, args=(I,))
    
    # Plot the results to visualize the dynamic system
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.title('FitzHugh-Nagumo Model')
    plt.plot(t, sol[:, 0], label='v(t)')
    plt.xlabel('Time')
    plt.ylabel('v')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(t, sol[:, 1], label='w(t)', color='orange')
    plt.xlabel('Time')
    plt.ylabel('w')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    print("Test for FitzHugh-Nagumo Model: Visual inspection required for pass/fail")
    
# Run the test
test_fitzhugh_nagumo_model()

