# Implementing the Shell Sort Algorithm
# Shell sort is a generalization of insertion sort that allows the exchange of items that are far apart.

def shell_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the shell sort algorithm.
    """
    n = len(arr)
    gap = n // 2  # Initialize the gap for comparison
    
    # Perform the shell sort
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap for the next iteration
        
    return arr

# Pytest test cases for shell sort

def test_shell_sort():
    assert shell_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert shell_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert shell_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert shell_sort([]) == []
    assert shell_sort([1]) == [1]

# Run the test
test_shell_sort()
