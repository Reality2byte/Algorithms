# Binary Exponentiation algorithm
def binary_exponentiation(a, b):
    """
    Calculate the result of a^b using the Binary Exponentiation algorithm.
    
    Parameters:
    a (int): The base number.
    b (int): The exponent.
    
    Returns:
    int: The result of a^b.
    """
    res = 1
    base = a
    while b > 0:
        if b % 2 == 1:
            res *= base
        base *= base
        b //= 2
    return res

# Pytest test cases for the Binary Exponentiation algorithm
def test_binary_exponentiation():
    assert binary_exponentiation(2, 3) == 8
    assert binary_exponentiation(5, 0) == 1
    assert binary_exponentiation(3, 4) == 81
    assert binary_exponentiation(7, 2) == 49

# Directly run the test function to validate the algorithm
test_binary_exponentiation()
print("All tests passed for Binary Exponentiation algorithm.")
