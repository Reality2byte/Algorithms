# Now let's implement the Kadane's Algorithm.
# This algorithm finds the largest sum contiguous subarray in an array of integers.
# It operates in O(n) time complexity.

def kadanes_algorithm(arr: List[int]) -> int:
    # Initialize variables to keep track of the maximum sum and the current sum
    max_sum = current_sum = arr[0]
    
    # Iterate through the array to find the maximum subarray sum
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Test the kadanes_algorithm function
def test_kadanes_algorithm():
    assert kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert kadanes_algorithm([1]) == 1
    assert kadanes_algorithm([-1, -2, -3, -4]) == -1
    assert kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19
    
# Run the tests and print the output
test_kadanes_algorithm()
print("All tests passed for Kadane's Algorithm!")
