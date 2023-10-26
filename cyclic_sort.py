# First Algorithm: Cyclic Sort
# This algorithm sorts an array containing 'n' objects numbered from 1 to 'n' in a cyclic way.
# It uses the cyclic sort algorithm to put the numbers in their correct position in O(n) time.

from typing import List

def cyclic_sort(nums: List[int]) -> List[int]:
    """
    Sort an array containing 'n' objects numbered from 1 to 'n' using cyclic sort.
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

# Importing pytest for writing test cases
import pytest

def test_cyclic_sort():
    # Test cases
    assert cyclic_sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5]
    assert cyclic_sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
    assert cyclic_sort([1]) == [1]
    assert cyclic_sort([]) == []
    print("All test cases for Cyclic Sort passed!")

# Run the test
test_cyclic_sort()
