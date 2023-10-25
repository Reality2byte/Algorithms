# Merge Sort Algorithm Implementation
def merge_sort(arr):
    """
    Sorts an array using Merge Sort algorithm.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    merge_sort(left_half)
    merge_sort(right_half)
    
    i = j = k = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    
    return arr

# Pytest test cases for Merge Sort
def test_merge_sort():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]

# Running the tests
test_merge_sort()

