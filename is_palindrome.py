# Implementing the Palindrome Checker Algorithm
# A palindrome is a word, phrase, or sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    return s == s[::-1]

# Pytest test cases for palindrome checker

def test_is_palindrome():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw") == True

# Run the test
test_is_palindrome()
