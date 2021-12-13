# In daily share trading, a buyer buys shares in the morning
# and sells them on the same day. If the trader is allowed to
# make at most 2 transactions in a day, whereas the second
# transaction can only start after the first one is complete (Buy->sell->Buy->sell).
# Given stock prices throughout the day, find out the maximum profit
# that a share trader could have made


# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75
# Buy at 10, sell at 22, 22 -10 = 12
# Buy at 5 and sell at 80 , 80 - 5 = 75
#
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80
#
# Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
# Output:  72
# Buy at price 8 and sell at 80.
# Input:   price[] = {90, 80, 70, 60, 50}
# Output:  0
# Not possible to earn.


# DP Solution__ Time complexity : O(n).
import sys


def maxProfits(prices):
    n = len(prices)
    # initialize dp with 0
    dp = [0 for _ in range(n)]

    max_price = prices[n - 1]
    for i in range(n - 2, 0, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        dp[i] = max(dp[i + 1], max_price - prices[i])

    min_price = prices[0]
    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
        dp[i] = max(dp[i - 1], dp[i] + (prices[i] - min_price))

    ans = dp[n - 1]
    return ans


# Another O(N) solution
def maxProfit(price):
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0

    for i in range(len(prices)):
        first_buy = max(first_buy, -price[i])
        first_sell = max(first_sell, first_buy + price[i])
        second_buy = max(second_buy, first_sell - price[i])
        second_sell = max(second_sell, second_buy + price[i])

    return second_sell


prices = [int(i) for i in input().strip().split()]
ans = maxProfit(prices)
print(ans)
