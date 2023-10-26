# Implementing and testing the Euclidean Algorithm for finding the greatest common divisor (GCD) of two numbers.
# The Euclidean Algorithm is a method for finding the greatest common divisor (GCD) of two integers.
# It is based on the principle that the GCD of two numbers a and b (where a > b) is the same as the GCD of b and a % b.

def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Pytest for the gcd function
def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(56, 48) == 8
    assert gcd(101, 103) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

# Run the test
test_gcd()
print("All gcd tests passed!")
