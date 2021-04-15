# A thief robbing a store can carry a maximal weight of W into his knapsack.
# There are N items, and i-th item weigh 'Wi' and the value being 'Vi.'
# What would be the maximum value V, that the thief can steal?
# Examples::
# Input 1:
# 4
# 1 2 4 5
# 5 4 8 6
# 5
# output 1: 13

# Input 2:
# 5
# 12 7 11 8 9
# 24 13 23 15 16
# 26
# output 2: 51

# Recursive solution::
def knapSackRec(weights, values, maxWeights, n):
    # base case:
    if (n == 0 or maxWeights == 0):
        return 0

    if (weights[n - 1] <= maxWeights):
        a = knapSackRec(weights, values, maxWeights, n - 1)
        b = values[n - 1] + knapSackRec(weights, values, maxWeights - weights[n - 1], n - 1)
        return max(a, b)
    else:
        return knapSackRec(weights, values, maxWeights, n - 1)


# Memoization::
def knapSackMemo(weights, values, maxWeights, n, dp):
    if n == 0 or maxWeights == 0:
        return 0

    if (weights[n - 1] > maxWeights):
        ans = knapSackMemo(weights, values, maxWeights, n - 1, dp)
        dp[n][maxWeights] = ans
        return ans
    else:
        if (dp[n][maxWeights] == -1):
            a = knapSackMemo(weights, values, maxWeights, n - 1, dp)
            b = values[n - 1] + knapSackMemo(weights, values, maxWeights - weights[n - 1], n - 1, dp)
            ans = max(a, b)
            dp[n][maxWeights] = ans
            return ans
        else:
            return dp[n][maxWeights]


# Iterative::
def knapSackIter(weights, values, maxWeight, n):
    dp = [[0 for j in range(maxWeight + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, maxWeight + 1):
            if w < weights[i - 1]:
                ans = dp[i - 1][w]
            else:
                ans1 = dp[i - 1][w]
                ans2 = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                ans = max(ans1, ans2)
            dp[i][w] = ans
    return dp[n][maxWeight]


def knapSack(weights, values, maxWeight, n):
    dp = [[-1 for i in range(maxWeight + 1)] for j in range(n + 1)]
    # return knapSackRec(weights, values, maxWeight, n)
    # return knapSackMemo(weights, values, maxWeight, n, dp)
    return knapSackIter(weights, values, maxWeight, n)


weights = [int(i) for i in input().strip().split()]
values = [int(i) for i in input().strip().split()]
wMax = int(input())
n = len(values)
ans = knapSack(weights, values, wMax, n)
print(ans)
