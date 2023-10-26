# Now let's implement the Rabin-Karp algorithm for substring search.
# The Rabin-Karp algorithm uses hashing to find a substring in a text.
# The algorithm has a worst-case time complexity of O(nm) but performs well in practice.

def rabin_karp(text: str, pattern: str) -> int:
    # Define a prime number to use in hash calculations
    prime = 101
    
    # Initialize variables for text and pattern lengths, and their hash values
    n, m = len(text), len(pattern)
    text_hash, pattern_hash = 0, 0
    
    # Calculate the initial hash values for the text and pattern
    for i in range(m):
        text_hash = (text_hash * prime + ord(text[i])) % prime
        pattern_hash = (pattern_hash * prime + ord(pattern[i])) % prime
    
    # Loop through the text to find the pattern
    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            # Double-check each character to confirm a match
            if text[i:i + m] == pattern:
                return i
        
        # Update the hash value for the next substring
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * (prime ** (m - 1))) * prime + ord(text[i + m]) % prime
            
    return -1

# Test the rabin_karp function
def test_rabin_karp():
    assert rabin_karp("hello world", "world") == 6
    assert rabin_karp("abcdef", "def") == 3
    assert rabin_karp("abcdef", "ghi") == -1
    assert rabin_karp("a", "a") == 0
    assert rabin_karp("this is a test", "test") == 10
    
# Run the tests and print the output
test_rabin_karp()
print("All tests passed for Rabin-Karp Algorithm!")
