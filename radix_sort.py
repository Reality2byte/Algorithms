# Next, let's implement the Radix Sort algorithm.
# Radix Sort is a non-comparative integer sorting algorithm.
# It sorts numbers digit-by-digit from the least significant digit to the most significant.

def counting_sort_for_radix(arr, exp):
    """
    A modified counting sort function to be used by the radix sort algorithm.
    
    Parameters:
        arr (list): The array to be sorted.
        exp (int): The digit's place value to sort by (1s, 10s, 100s, etc.).
        
    Returns:
        list: A new list containing the sorted elements based on the digit's place value.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
        
    return output

# It seems there was a bug in the radix_sort function while handling an empty array.
# I'll fix the bug by checking for an empty array before calling max().

def radix_sort(arr):
    """
    Sort an array using the Radix Sort algorithm.
    
    Parameters:
        arr (list): The array to be sorted.
        
    Returns:
        list: A new list containing the sorted elements.
    """
    if len(arr) == 0:
        return []
    
    max_val = max(arr)
    exp = 1
    sorted_arr = arr.copy()
    
    while max_val // exp > 0:
        sorted_arr = counting_sort_for_radix(sorted_arr, exp)
        exp *= 10
        
    return sorted_arr


# Now let's write tests to validate the implementation.
def test_radix_sort():
    """
    Test the radix_sort function.
    """
    # Test on an empty array
    assert radix_sort([]) == []
    
    # Test on an array with one element
    assert radix_sort([1]) == [1]
    
    # Test on an array with multiple elements
    assert radix_sort([4, 2, 7, 1, 9, 3]) == [1, 2, 3, 4, 7, 9]

# Run the tests
test_radix_sort()
print("All tests for Radix Sort passed!")
