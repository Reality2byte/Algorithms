# Fibonacci Sequence Algorithm Implementation using Recursion
def fibonacci_recursive(n):
    """
    Generates the nth Fibonacci number using recursion.
    :param n: The position of the Fibonacci number to generate
    :return: The nth Fibonacci number
    """
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Pytest test cases for Fibonacci Sequence using Recursion
def test_fibonacci_recursive():
    assert fibonacci_recursive(1) == 0
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 1
    assert fibonacci_recursive(4) == 2
    assert fibonacci_recursive(5) == 3
    assert fibonacci_recursive(0) == "Invalid input"
    assert fibonacci_recursive(-1) == "Invalid input"

# Running the tests
test_fibonacci_recursive()

