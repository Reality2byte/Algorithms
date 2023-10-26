# Implementing the Heap Sort Algorithm
# Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure.

from heapq import heapify, heappop

def heap_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the heap sort algorithm.
    """
    heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heappop(arr))
    return sorted_arr

# Pytest test cases for heap sort

def test_heap_sort():
    assert heap_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert heap_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert heap_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]

# Run the test
test_heap_sort()
