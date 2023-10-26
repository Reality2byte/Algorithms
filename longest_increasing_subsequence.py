# Fifth Algorithm: Longest Increasing Subsequence
# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
# such that all elements of the subsequence are sorted in increasing order.

from typing import List

def longest_increasing_subsequence(arr: List[int]) -> int:
    """
    Find the length of the longest increasing subsequence from the given list.
    """
    n = len(arr)
    if n == 0:
        return 0
    
    # Initialize lengths to be 1 for all indexes
    lengths = [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lengths[i] = max(lengths[i], lengths[j] + 1)
                
    return max(lengths)

# Test cases for Longest Increasing Subsequence
def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert longest_increasing_subsequence([3, 4, 2, 8, 10]) == 4
    assert longest_increasing_subsequence([3, 2]) == 1
    assert longest_increasing_subsequence([]) == 0
    print("All test cases for Longest Increasing Subsequence passed!")

# Run the test
test_longest_increasing_subsequence()
