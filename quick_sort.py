# Quick Sort Algorithm Implementation
def quick_sort(arr):
    """
    Sorts an array using Quick Sort algorithm.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Pytest test cases for Quick Sort
def test_quick_sort():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quick_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([3, 2, 1]) == [1, 2, 3]

# Running the tests
test_quick_sort()

