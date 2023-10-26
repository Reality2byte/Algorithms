# Sixth Algorithm: Z-Algorithm for String Matching
# The Z-Algorithm builds a Z-array in linear time, which helps in pattern matching within a string.

def z_algorithm(text: str) -> List[int]:
    """
    Calculate the Z-array for the given string.
    Z[i] represents the length of the longest substring starting from i which is also a prefix of the string.
    """
    n = len(text)
    z_array = [0] * n
    
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z_array[i] = min(r - i + 1, z_array[i - l])
        
        while i + z_array[i] < n and text[z_array[i]] == text[i + z_array[i]]:
            z_array[i] += 1
        
        if i + z_array[i] - 1 > r:
            l, r = i, i + z_array[i] - 1
            
    return z_array

# Test cases for Z-Algorithm
def test_z_algorithm():
    assert z_algorithm("aabcaabxaaaz") == [0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0]
    assert z_algorithm("aaaaaa") == [0, 5, 4, 3, 2, 1]
    assert z_algorithm("abracadabra") == [0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 1]
    print("All test cases for Z-Algorithm passed!")

# Run the test
test_z_algorithm()
