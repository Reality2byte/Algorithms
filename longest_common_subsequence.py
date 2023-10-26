# Next, let's implement the Longest Common Subsequence (LCS) algorithm.
# The LCS algorithm finds the longest subsequence common to two sequences.
# It operates in O(m * n) time, where m and n are the lengths of the two sequences.

def longest_common_subsequence(s1: str, s2: str) -> int:
    # Initialize a 2D array to store the lengths of LCS of substrings
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Build up the dp array
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp[-1][-1]

# Test the longest_common_subsequence function
def test_longest_common_subsequence():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("bluesky", "sky") == 3
    assert longest_common_subsequence("stone", "longest") == 3
    
# Run the tests and print the output
test_longest_common_subsequence()
print("All tests passed for Longest Common Subsequence!")
