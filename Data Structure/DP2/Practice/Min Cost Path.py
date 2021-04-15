import sys


def minCostPathRec(mat, i, j, row, col):
    if i == row - 1 and j == col - 1:
        return mat[i][j]
    if i >= row or j >= col:
        return sys.maxsize
    # right
    ans1 = minCostPathRec(mat, i, j + 1, row, col)
    # down
    ans2 = minCostPathRec(mat, i + 1, j, row, col)
    # diagonal
    ans3 = minCostPathRec(mat, i + 1, j + 1, row, col)
    ans = mat[i][j] + min(ans1, ans2, ans3)
    return ans


def minCostPathMemo(mat, i, j, row, col, dp):
    if i == row - 1 and j == col - 1:
        return mat[i][j]
    if i >= row or j >= col:
        return sys.maxsize
    # diagonal
    if dp[i + 1][j + 1] == -1:
        a = minCostPathMemo(mat, i + 1, j + 1, row, col, dp)
        dp[i + 1][j + 1] = a
    else:
        a = dp[i + 1][j + 1]
    # down
    if dp[i + 1][j] == -1:
        b = minCostPathMemo(mat, i + 1, j, row, col, dp)
        dp[i + 1][j] = b
    else:
        b = dp[i + 1][j]
    # right
    if dp[i][j + 1] == -1:
        c = minCostPathMemo(mat, i, j + 1, row, col, dp)
        dp[i][j + 1] = c
    else:
        c = dp[i][j + 1]

    ans = mat[i][j] + min(a, b, c)
    return ans


def minCostPathIter():
    pass


def minCostPath(mat, row, col):
    i, j = 0, 0
    dp = [[-1 for j in range(col + 1)] for i in range(row + 1)]
    # ans = minCostPathRec(mat, i, j, row, col)
    ans = minCostPathMemo(mat, i, j, row, col, dp)
    # ans = minCostM(mat, i, j, row, col, dp)
    return ans


row_col = [int(i) for i in input().strip().split()]
# Main
row = row_col[0]
col = row_col[1]
mat = [[int(i) for i in input().strip().split()] for j in range(row)]
print(minCostPath(mat, row, col))
