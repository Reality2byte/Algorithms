# Third Algorithm: Factorial using Dynamic Programming
# Calculating the factorial of a number using dynamic programming to save previously computed values.

from typing import Dict

def factorial_dp(n: int, memo: Dict[int, int] = {}) -> int:
    """
    Calculate the factorial of a number using dynamic programming.
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1
    
    memo[n] = n * factorial_dp(n - 1, memo)
    return memo[n]

# Test cases for Factorial using Dynamic Programming
def test_factorial_dp():
    assert factorial_dp(0) == 1
    assert factorial_dp(1) == 1
    assert factorial_dp(5) == 120
    assert factorial_dp(7) == 5040
    assert factorial_dp(10) == 3628800
    print("All test cases for Factorial using Dynamic Programming passed!")

# Run the test
test_factorial_dp()
