import sys


# Recursive_____________________________________________________________________________________________________________
def minCostR(mat, i, j, row, col):
    if i == row - 1 and j == col - 1:
        return mat[i][j]

    if i >= row or j >= col:
        return sys.maxsize

    a = minCostR(mat, i + 1, j + 1, row, col)
    b = minCostR(mat, i + 1, j, row, col)
    c = minCostR(mat, i, j + 1, row, col)
    ans = mat[i][j] + min(a, b, c)
    return ans


# Memoization___________________________________________________________________________________________________________
def minCostM(mat, i, j, row, col, dp):
    if i == row - 1 and j == col - 1:
        return mat[i][j]

    if i >= row or j >= col:
        return sys.maxsize

    if dp[i + 1][j + 1] == -1:
        a = minCostM(mat, i + 1, j + 1, row, col, dp)
        dp[i + 1][j + 1] = a
    else:
        a = dp[i + 1][j + 1]
    if dp[i + 1][j] == -1:
        b = minCostM(mat, i + 1, j, row, col, dp)
        dp[i + 1][j] = b
    else:
        b = dp[i + 1][j]

    if dp[i][j + 1] == -1:
        c = minCostM(mat, i, j + 1, row, col, dp)
        dp[i][j + 1] = c
    else:
        c = dp[i][j + 1]

    ans = mat[i][j] + min(a, b, c)
    return ans


# Iterative_____________________________________________________________________________________________________________
def minCostIterativeTD(cost, n, m):
    DP = [[sys.maxsize for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                DP[i][j] = cost[0][0]
            else:
                ans1 = DP[i - 1][j]
                ans2 = DP[i][j - 1]
                ans3 = DP[i - 1][j - 1]
                DP[i][j] = cost[i - 1][j - 1] + min(ans1, ans2, ans3)
    return DP[n][m]


def minCostIterativeBU(cost, n, m):
    dp = [[sys.maxsize for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n - 1 and j == m - 1:
                dp[i][j] = cost[i][j]
            else:
                ans1 = dp[i + 1][j]
                ans2 = dp[i][j + 1]
                ans3 = dp[i + 1][j + 1]
                dp[i][j] = cost[i][j] + min(ans1, ans2, ans3)
    return dp[0][0]


# Driver_________________________________________________________________________________________________________________
a = [int(i) for i in input().strip().split()]
n = a[0]
m = a[1]
mat = [[int(i) for i in input().strip().split()] for x in range(n)]
dp = [[sys.maxsize for j in range(m + 1)] for i in range(n + 1)]
DP = [[-1 for j in range(m + 1)] for i in range(n + 1)]

print(minCostR(mat, 0, 0, n, m))
# print(minCostM(mat, 0, 0, n, m, DP))
# print(minCostIterativeBU(mat, n, m))
