# Implementing and testing the Levenshtein Distance Algorithm
# Levenshtein distance is a measure of the similarity between two strings.
# It is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one string into the other.

def levenshtein_distance(str1, str2):
    """
    Compute the Levenshtein distance between two strings.
    """
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
    return dp[m][n]

# Pytest for the levenshtein_distance function
def test_levenshtein_distance():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("flaw", "lawn") == 2
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance("apple", "apple") == 0
    assert levenshtein_distance("apple", "") == 5
    assert levenshtein_distance("", "apple") == 5

# Run the test
test_levenshtein_distance()
print("All levenshtein_distance tests passed!")
