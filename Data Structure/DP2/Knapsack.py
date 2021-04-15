def knapsackBF(weights, values, maxWeight):
    n = len(weights)
    return knapsackREC(weights, values, maxWeight, n)


def knapsackREC(weights, values, maxWeight, n):
    if n == 0 or maxWeight == 0:
        return 0

    if weights[n - 1] > maxWeight:
        return knapsackREC(weights, values, maxWeight, n - 1)

    including_item = values[n - 1] + knapsackREC(weights, values, maxWeight - weights[n - 1], n - 1)
    excluding_item = knapsackREC(weights, values, maxWeight, n - 1)

    return max(including_item, excluding_item)


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
weights = list(int(i) for i in input().strip().split(' '))
values = list(int(i) for i in input().strip().split(' '))
maxWeight = int(input())
print(knapsackBF(weights, values, maxWeight))
