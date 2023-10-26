# Implementing the Selection Sort Algorithm
# Selection sort is a simple comparison-based sorting algorithm.
# It works by repeatedly selecting the minimum (or maximum) element from an unsorted subarray and putting it at the beginning (or end).

from typing import List
import pytest

def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the selection sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

# Pytest test cases for selection sort

def test_selection_sort():
    assert selection_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert selection_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert selection_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]

# Run the test
pytest.main(["-v", "-k", "test_selection_sort"])
