# Consider a row of n coins of values v1 . . . vn, where n is even.
# We play a game against an opponent by alternating turns. In each turn,
# a player selects either the first or last coin from the row, removes it
# from the row permanently, and receives the value of the coin. Determine
# the maximum possible amount of money we can definitely win if we move first.

# NOTE: The opponent is as clever as the user.
#
# Let us understand the problem with few examples:
#
# 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)
# 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)
# Does choosing the best at each move gives an optimal solution? No.
# In the second example, this is how the game can be finished:
#
# …….User chooses 8.
# …….Opponent chooses 15.
# …….User chooses 7.
# …….Opponent chooses 3.
# Total value collected by user is 15(8 + 7)
# …….User chooses 7.
# …….Opponent chooses 8.
# …….User chooses 15.
# …….Opponent chooses 3.
# Total value collected by user is 22(7 + 15)
# So if the user follows the second game state, the maximum value can be collected although the first move is not the best.

def max_coinRec(coins, start, end):
    if start > end:
        return 0

    a = coins[start] + min(max_coinRec(coins, start + 2, end), max_coinRec(coins, start + 1, end - 1))
    b = coins[end] + min(max_coinRec(coins, start + 1, end - 1), max_coinRec(coins, start, end - 2))
    return max(a, b)


def max_coinsMemo(coins, start, end, dp):
    if end == start + 1:
        return max(coins[start], coins[end])

    if dp[start][end] != -1:
        return dp[start][end]
    else:
        a = coins[start] + min(max_coinsMemo(coins, start + 2, end, dp), max_coinsMemo(coins, start + 1, end - 1, dp))
        b = coins[end] + min(max_coinsMemo(coins, start + 1, end - 1, dp), max_coinsMemo(coins, start, end - 2, dp))
        dp[start][end] = max(a, b)
        return dp[start][end]


coins = [int(i) for i in input().strip().split()]
start = 0
end = len(coins)
print(max_coinRec(coins, start, end - 1))
dp = [[-1 for i in range(100)] for j in range(100)]
print(max_coinsMemo(coins, start, end, dp))
