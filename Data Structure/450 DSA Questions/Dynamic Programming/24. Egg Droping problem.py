import sys


def eggDropRec(n, k):
    if k == 1 or k == 0:
        return k
    if n == 1:
        return k

    minimum = sys.maxsize
    for floor in range(1, k):
        res = 1 + max(eggDropRec(n - 1, floor - 1), eggDropRec(n, k - floor))
        if res < minimum:
            minimum = res
    return minimum


def eggDropDp(n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = 1
        dp[i][0] = 0

    for j in range(1, k + 1):
        dp[1][j] = j

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = sys.maxsize
            for floor in range(1, j + 1):
                res = 1 + max(dp[i - 1][floor - 1], dp[i][j - floor])
                if res < dp[i][j]:
                    dp[i][j] = res
    return dp[n][k]


eggs = int(input())
floors = int(input())

# print(eggDropRec(eggs, floors))
print(eggDropDp(eggs, floors))
