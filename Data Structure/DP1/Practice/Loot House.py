def maxMoneyLootedREC(houses, n):
    if n <= 0:
        return 0

    including_house = houses[n - 1] + maxMoneyLootedREC(houses, n - 2)
    excluding_house = maxMoneyLootedREC(houses, n - 1)
    return max(including_house, excluding_house)


def maxMoneyLootedMEM(houses, n, dp):
    if n <= 0:
        return 0

    if dp[n] == -1:
        ans1 = houses[n - 1] + maxMoneyLootedMEM(houses, n - 2, dp)
        ans2 = maxMoneyLootedMEM(houses, n - 1, dp)
        ans = max(ans1, ans2)
        dp[n] = ans
        return dp[n]
    else:
        ans = dp[n]
        return ans




# _Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(maxMoneyLootedREC(arr, n))
dp = [-1 for i in range(n + 1)]
print(maxMoneyLootedMEM(arr, n, dp))
