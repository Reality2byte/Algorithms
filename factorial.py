import pytest

# Factorial algorithm using recursion
def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.
    
    Parameters:
    n (int): A non-negative integer.
    
    Returns:
    int: The factorial of the given integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Pytest test cases for the factorial algorithm
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    
    with pytest.raises(ValueError):
        factorial(-1)

# Run the test and display the output
pytest.main(["-v", "-k test_factorial"], exit=False)
