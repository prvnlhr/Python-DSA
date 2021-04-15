import sys


def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit


prices = [int(i) for i in input().strip().split()]
ans = maxProfit(prices)
print(ans)
