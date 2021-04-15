# _Recursive:
def knapsackREC(weights, values, maxWeight, n):
    if n == 0 or maxWeight == 0:
        return 0

    if weights[n - 1] > maxWeight:
        return knapsackREC(weights, values, maxWeight, n - 1)

    including_item = values[n - 1] + knapsackREC(weights, values, maxWeight - weights[n - 1], n - 1)
    excluding_item = knapsackREC(weights, values, maxWeight, n - 1)
    ans = max(including_item, excluding_item)
    return ans


# _Memoization:
def knapsackMemo(weights, values, maxWeight, n, dp):
    if n == 0 or maxWeight == 0:
        return 0
    if weights[n - 1] > maxWeight:
        ans = knapsackMemo(weights, values, maxWeight, n - 1, dp)
        dp[n][maxWeight] = ans
        return ans

    else:
        if dp[n][maxWeight] == -1:
            including_item = values[n - 1] + knapsackMemo(weights, values, maxWeight - weights[n - 1], n - 1, dp)
            excluding_item = knapsackMemo(weights, values, maxWeight, n - 1, dp)
            ans = max(including_item, excluding_item)
            dp[n][maxWeight] = ans
            return ans
        else:
            ans = dp[n][maxWeight]
            return ans


# _Iterative:
def knapsackIterTD(weights, values, maxWeight):
    n = len(values)
    dp = [[0 for j in range(maxWeight + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, maxWeight + 1):
            if j < weights[i - 1]:
                ans = dp[i - 1][j]
            else:
                ans1 = values[i - 1] + dp[i - 1][j - weights[i - 1]]
                ans2 = dp[i - 1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans

    return dp[n][maxWeight]


n = int(input())
weights = [int(i) for i in input().strip().split()]
values = [int(j) for j in input().strip().split()]
maxWeight = int(input())
# print(knapsackREC(weights, values, maxWeight, n))
N = len(values)
dp = [[-1 for i in range(maxWeight + 1)] for j in range(N + 1)]
# print(knapsackMemo(weights, values, maxWeight, n, dp))
print(knapsackIterTD(weights, values, maxWeight))
