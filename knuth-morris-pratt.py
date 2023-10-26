def kmp_search(text, pattern):
    """
    Knuth-Morris-Pratt (KMP) algorithm for substring search.
    
    Parameters:
    text (str): The text string to search within.
    pattern (str): The pattern string to search for.
    
    Returns:
    list: A list of starting indices where the pattern is found in the text.
    """
    # Create the longest prefix suffix (lps) array for the pattern
    lps = [0] * len(pattern)
    j = 0  # Length of the previous longest prefix suffix
    
    # Preprocess the pattern to populate the lps array
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j-1]
            
        if pattern[j] == pattern[i]:
            j += 1
            lps[i] = j
    
    # Search for the pattern in the text using the lps array
    i, j = 0, 0  # Pointers for text and pattern
    occurrences = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == len(pattern):
                occurrences.append(i - j)
                j = lps[j-1]
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return occurrences

# Pytest test cases
def test_kmp_search():
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AAAAABAAABA", "AAAA") == [0, 1, 2]
    assert kmp_search("THIS IS A TEST TEXT", "TEST") == [10]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("HELLO WORLD", "WORLD") == [6]
    assert kmp_search("HELLO WORLD", "WORLDS") == []
    
# Run the test
test_kmp_search()
print("KMP string search algorithm test passed.")
