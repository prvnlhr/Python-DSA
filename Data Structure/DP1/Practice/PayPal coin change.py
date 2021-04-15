# def coinChange(n):
#     if n == 1 or n == 0:
#         return n
#
#     a = coinChange(n - 25)
#     b = coinChange(n - 10)
#     c = coinChange(n - 5)
#     d = coinChange(n - 1)
#     ans = a + b + c + d
#     return min(ans, n)
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    print(dp)
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1


coins = [int(i) for i in input().strip().split()]
amount = int(input())
ans = coinChange(coins, amount)
print(ans)
