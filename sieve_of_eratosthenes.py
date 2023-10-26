# Sieve of Eratosthenes algorithm
def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.
    
    Parameters:
    n (int): The limit up to which prime numbers are to be found.
    
    Returns:
    list: A list of prime numbers up to the given limit.
    """
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [x for x in range(2, n + 1) if primes[x]]

# Pytest test cases for the Sieve of Eratosthenes algorithm
def test_sieve_of_eratosthenes():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(0) == []
    assert sieve_of_eratosthenes(2) == [2]

# Directly run the test function to validate the algorithm
test_sieve_of_eratosthenes()
print("All tests passed for Sieve of Eratosthenes algorithm.")
