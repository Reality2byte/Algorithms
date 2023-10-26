# Next, let's implement the Boyer-Moore string search algorithm.
# The Boyer-Moore algorithm is an efficient string searching (substring finding) algorithm.
# It skips sections of the text to result in a lower number of overall character comparisons.

def build_bad_character_table(pattern):
    """
    Build the bad character table for Boyer-Moore algorithm.
    
    Parameters:
    pattern (str): The pattern string.
    
    Returns:
    dict: A dictionary mapping each character in the pattern to its last occurrence index.
    """
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table

def boyer_moore_search(text, pattern):
    """
    Search for the pattern in the text using Boyer-Moore algorithm.
    
    Parameters:
    text (str): The text string.
    pattern (str): The pattern string.
    
    Returns:
    int: The starting index of the first occurrence of the pattern in the text, or -1 if not found.
    """
    m, n = len(pattern), len(text)
    bad_char_table = build_bad_character_table(pattern)
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            return i
        else:
            i += max(1, j - bad_char_table.get(text[i + j], -1))
    
    return -1

# Test the Boyer-Moore string search algorithm implementation
def test_boyer_moore_search():
    assert boyer_moore_search("hello world", "world") == 6
    assert boyer_moore_search("hello world", "hello") == 0
    assert boyer_moore_search("hello world", "o w") == 4
    assert boyer_moore_search("hello world", "not") == -1

# Run the test and print the output
test_boyer_moore_search()
"Boyer-Moore string search algorithm test passed!"
