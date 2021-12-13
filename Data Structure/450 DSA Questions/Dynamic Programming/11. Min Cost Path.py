import sys


# Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost
# of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to
# traverse through that cell. The total cost of a path to reach (m, n) is the sum of all the costs
# on that path (including both source and destination). You can only traverse down, right and
# diagonally lower cells from a given cell, i.e., from a given cell (i, j),
# cells (i + 1, j), (i, j + 1), and (i + 1, j + 1) can be traversed.
# You may assume that all costs are positive integers.

# Ex__
# 1  2  3
# 4  8  2
# 1  5  3
#
# The path with minimum cost is (0, 0) –> (0, 1) –> (1, 2) –> (2, 2).
# The cost of the path is 8 (1 + 2 + 2 + 3).

# 1) Optimal Substructure
# The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1).
# So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.
# minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]
#
# 2) Overlapping SubProblems
# Following is a simple recursive implementation of the MCP (Minimum Cost Path) problem.
# The implementation simply follows the recursive structure mentioned above.


def minCostRec(mat, i, j, row, col):
    if i == row - 1 and j == col - 1:
        return mat[i][j]
    if i >= row or j >= col:
        return sys.maxsize

    a = minCostRec(mat, i + 1, j + 1, row, col)
    b = minCostRec(mat, i + 1, j, row, col)
    c = minCostRec(mat, i, j + 1, row, col)
    ans = mat[i][j] + min(a, b, c)
    return ans


def minCostMemo(mat, i, j, row, col, dp):
    if i == row - 1 and j == col - 1:
        return mat[i][j]
    if i >= row or j >= col:
        return sys.maxsize

    if dp[i + 1][j + 1] == -1:
        a = minCostMemo(mat, i + 1, j + 1, row, col, dp)
        dp[i + 1][j + 1] = a
    else:
        a = dp[i + 1][j + 1]
    if dp[i + 1][j] == -1:
        b = minCostMemo(mat, i + 1, j, row, col, dp)
        dp[i + 1][j] = b
    else:
        b = dp[i + 1][j]

    if dp[i][j + 1] == -1:
        c = minCostMemo(mat, i, j + 1, row, col, dp)
        dp[i][j + 1] = c
    else:
        c = dp[i][j + 1]

    ans = mat[i][j] + min(a, b, c)
    return ans


def minCostPath(mat):
    row = len(mat)
    col = len(mat[0])
    dp = [[-1 for i in range(col + 1)] for j in range(row + 1)]
    print(row, col, dp)
    # ans = minCostRec(mat, 0, 0, row, col)
    ans = minCostMemo(mat, 0, 0, row, col, dp)
    return ans


nRows = int(input())
mat = [[int(i) for i in input().strip().split()] for j in range(nRows)]
print(mat)
print(minCostPath(mat))
