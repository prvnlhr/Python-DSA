import sys


# O(N) VALLEY PEAK algorithm
# In this approach, we just need to find the next greater element
# and subtract it from the current element so that the difference
# keeps increasing until we reach a minimum. If the sequence is a
# decreasing sequence so the maximum profit possible is 0.

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            curr_profit = prices[i] - prices[i - 1]
            profit = profit + curr_profit

    return profit


prices = [int(i) for i in input().strip().split()]
ans = maxProfit(prices)
print(ans)
