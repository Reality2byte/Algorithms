# Debugging: Print the lps array and occurrences to find what is going wrong
def kmp_search_debug(text, pattern):
    # Create the longest prefix suffix (lps) array for the pattern
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    
    # Preprocess the pattern to populate the lps array
    for i in range(1, len(pattern)):
        while length > 0 and pattern[length] != pattern[i]:
            length = lps[length-1]
            
        if pattern[length] == pattern[i]:
            length += 1
            lps[i] = length
    
    print(f"lps: {lps}")  # Debugging line
    
    # Search for the pattern in the text using the lps array
    i, j = 0, 0  # Pointers for text and pattern
    occurrences = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == len(pattern):
                occurrences.append(i - j)
                j = lps[j-1]  # Reset j to allow for overlapping occurrences
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    print(f"occurrences: {occurrences}")  # Debugging line
    
    return occurrences

# Debugging: Run the failing test case and print debug information
kmp_search_debug("AAAAABAAABA", "AAAA")  # Expected: [0, 1, 2]
