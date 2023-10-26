# Insertion sort algorithm
def insertion_sort(arr):
    """
    Sort a list of comparable elements using the insertion sort algorithm.
    
    Parameters:
    arr (list): A list of elements to be sorted.
    
    Returns:
    list: A sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Pytest test cases for the insertion sort algorithm
def test_insertion_sort():
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []
    assert insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Directly run the test function to validate the algorithm
test_insertion_sort()
print("All tests passed for insertion sort algorithm.")
