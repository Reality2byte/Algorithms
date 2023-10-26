# Implementing and testing the Coin Change Problem using Dynamic Programming
# The coin change problem is the problem of finding the minimum number of coins that sum up to a given value.
# Here, we assume that we have infinite supply of each of coin denominations.

def coin_change(coins, amount):
    """
    Compute the minimum number of coins that make up a given amount.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Pytest for the coin_change function
def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 2) == 2
    assert coin_change([1], 0) == 0
    assert coin_change([1], 1) == 1
    assert coin_change([186, 419, 83, 408], 6249) == 20

# Run the test
test_coin_change()
print("All coin_change tests passed!")
