# Linear search algorithm
def linear_search(arr, target):
    """
    Search for a target element in a list using linear search.
    
    Parameters:
    arr (list): A list of elements to be searched.
    target: The element to be searched for.
    
    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Pytest test cases for the linear search algorithm
def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    assert linear_search([], 1) == -1
    assert linear_search([1], 1) == 0

# Directly run the test function to validate the algorithm
test_linear_search()
print("All tests passed for linear search algorithm.")
