import sys


# Time complexity : O(kn) , Space complexity : O(nk).

def maxProfit(prices, k):
    n = len(prices)

    profit = [[0 for _ in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        prev_diff = -sys.maxsize
        for j in range(1, n):
            prev_diff = max(prev_diff, profit[i - 1][j - 1] - prices[j - 1])
            profit[i][j] = max(profit[i][j - 1], prices[j] + prev_diff)

    return profit[k][n - 1]


prices = [int(i) for i in input().strip().split()]
k = int(input())
ans = maxProfit(prices, k)
print(ans)
