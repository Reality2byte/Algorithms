# Let's start with the implementation of the Fisher-Yates Shuffle Algorithm.
# This algorithm is used to shuffle an array or list in a random manner.

import random
import pytest

def fisher_yates_shuffle(arr):
    """
    Shuffle an array using Fisher-Yates Shuffle Algorithm.
    
    Parameters:
        arr (list): The array to be shuffled.
        
    Returns:
        list: A new list containing the shuffled elements.
    """
    shuffled_arr = arr.copy()
    n = len(shuffled_arr)
    
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_arr[i], shuffled_arr[j] = shuffled_arr[j], shuffled_arr[i]
        
    return shuffled_arr


# Now let's write tests to validate the implementation.
def test_fisher_yates_shuffle():
    """
    Test the fisher_yates_shuffle function.
    """
    # Seed for reproducibility
    random.seed(42)
    
    # Test on an empty array
    assert fisher_yates_shuffle([]) == []
    
    # Test on an array with one element
    assert fisher_yates_shuffle([1]) == [1]
    
    # Test on an array with multiple elements
    arr = [1, 2, 3, 4, 5]
    shuffled_arr = fisher_yates_shuffle(arr)
    
    # Check that the shuffled array has the same length as the original array
    assert len(shuffled_arr) == len(arr)
    
    # Check that the shuffled array contains all the elements from the original array
    assert set(shuffled_arr) == set(arr)
    
    # Check that the shuffled array is not the same as the original array
    assert shuffled_arr != arr
    
    # Reset seed for subsequent tests
    random.seed(None)

# Run the tests
pytest.main(['-v', '-k', 'test_fisher_yates_shuffle'])
