import math, sys

# Given a value V, if we want to make change for V cents,
# and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins,
# what is the minimum number of coins to make the change?
#
# Examples:
#
# Input: coins[] = {25, 10, 5}, amount = 30
# Output: Minimum 2 coins required
# We can use one coin of 25 cents and one of 5 cents
#
# Input: coins[] = {9, 6, 5, 1}, amount = 11
# Output: Minimum 2 coins required
# We can use one coin of 6 cents and 1 coin of 5 cents


INF = math.inf


def coinChangeRec(coins, amount):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    ans = INF
    for coin in coins:
        if coin <= amount:
            a = 1 + coinChangeRec(coins, amount - coin)
            ans = min(ans, a)
    return ans


def coinChange(coins, amount):  # Example: coins = [1 2 5], amount = 5

    # amount   =  0  1   2   3   4   5
    # dp = [0  inf inf inf inf inf]
    dp = [float('inf') for _ in range(amount + 1)]
    # Only 1 way to make `0` change: return 0 coin
    dp[0] = 0

    # 1st pass: coin = 1 -> dp = [0 1 2 3 4 5]
    # 2nd pass: coin = 2 -> dp = [0 1 1 2 2 3]
    # 3rd pass: coin = 5 -> dp = [0 1 1 2 2 1]
    for coin in coins:
        for target in range(1, len(dp)):
            # If coin can be used to make up part of the amount
            if coin <= target:
                # Try use it and check what the min number of coins to make up
                # the rest `dp[target-coin]` and add 1 (rest + current coin)
                dp[target] = min(dp[target], dp[target - coin] + 1)

    # if dp[amount] couldn't be used then no
    # combination of coins could make up target amount
    return dp[amount] if dp[amount] != float('inf') else -1


coins = [int(i) for i in input().strip().split()]
amount = int(input())
ans = coinChangeRec(coins, amount)
# ans = coinChange(coins, amount)

print(ans)
