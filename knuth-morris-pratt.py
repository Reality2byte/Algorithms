# Next, let's implement the Knuth-Morris-Pratt (KMP) algorithm for substring search.
# The KMP algorithm preprocesses the pattern to identify any possible "fallback" positions that can be safely skipped.
# The algorithm has a time complexity of O(n + m), where n and m are the lengths of the text and pattern, respectively.

def kmp(text: str, pattern: str) -> int:
    # Initialize variables for text and pattern lengths
    n, m = len(text), len(pattern)
    
    # Create the longest prefix suffix (lps) array for the pattern
    lps = [0] * m
    j = 0  # Length of the previous longest prefix suffix
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    
    # Search for the pattern in the text using the lps array
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return -1

# Test the kmp function
def test_kmp():
    assert kmp("hello world", "world") == 6
    assert kmp("abcdef", "def") == 3
    assert kmp("abcdef", "ghi") == -1
    assert kmp("a", "a") == 0
    assert kmp("this is a test", "test") == 10
    
# Run the tests and print the output
test_kmp()
print("All tests passed for KMP Algorithm!")
