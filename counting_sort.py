# Let's start by implementing the Counting Sort algorithm.
# Counting Sort is an integer sorting algorithm and operates in O(n) time, given that the input range is known and not too large.
# It counts the occurrences of each element in the input, and then places them in their correct sorted position.

from typing import List
import pytest

def counting_sort(arr: List[int], maximum: int) -> List[int]:
    # Create a count array and initialize all elements to 0
    count_arr = [0] * (maximum + 1)
    
    # Populate count_arr with the frequency of each element in arr
    for num in arr:
        count_arr[num] += 1
    
    # Initialize variables for the sorted array and to keep track of the current index in count_arr
    sorted_arr = []
    current_index = 0
    
    # Construct the sorted array using the count_arr
    for i in range(len(count_arr)):
        while count_arr[i] > 0:
            sorted_arr.append(i)
            count_arr[i] -= 1
            current_index += 1
            
    return sorted_arr

# Test the counting_sort function
def test_counting_sort():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1], 8) == [1, 2, 2, 3, 3, 4, 8]
    assert counting_sort([1], 1) == [1]
    assert counting_sort([], 0) == []
    assert counting_sort([4, 7, 2, 5, 3, 6, 1, 8], 8) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert counting_sort([1, 1, 1, 1, 1, 1, 1, 1], 1) == [1, 1, 1, 1, 1, 1, 1, 1]
    
# Run the tests and print the output
pytest.main(["-v", "-s"], exit=False)
