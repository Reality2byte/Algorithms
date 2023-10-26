# Implementing the Kadane's Algorithm for Maximum Subarray Sum
# Kadane's algorithm is used to find the largest sum contiguous subarray in a one-dimensional array.

def max_subarray_sum(arr: List[int]) -> int:
    """
    Finds the maximum subarray sum using Kadane's algorithm.
    """
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

# Pytest test cases for Kadane's algorithm

def test_max_subarray_sum():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1, 2, 3, -2, 5]) == 9
    assert max_subarray_sum([-1, -2, -3, -4]) == -1
    assert max_subarray_sum([3, -1, -1, 3, 5, -1, -1]) == 9

# Run the test
test_max_subarray_sum()
