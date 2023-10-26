# Euclidean algorithm for calculating the Greatest Common Divisor (GCD)
def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The GCD of the two integers.
    """
    while b:
        a, b = b, a % b
    return a

# Pytest test cases for the GCD algorithm
def test_gcd():
    assert gcd(56, 48) == 8
    assert gcd(101, 103) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

# Directly run the test function to validate the algorithm
test_gcd()
print("All tests passed for GCD algorithm.")
