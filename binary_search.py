# Binary Search Algorithm Implementation
def binary_search(arr, target):
    """
    Searches for a target element in a sorted array using Binary Search algorithm.
    :param arr: Sorted list of elements
    :param target: Element to be searched
    :return: Index of the target if found, otherwise -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Pytest test cases for Binary Search
def test_binary_search():
    assert binary_search([2, 3, 4, 10, 40], 10) == 3
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([1], 1) == 0

# Running the tests
test_binary_search()

