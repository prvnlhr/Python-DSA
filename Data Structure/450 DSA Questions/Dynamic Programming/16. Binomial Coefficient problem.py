# The value of C(n, k) can be recursively calculated using
# the following standard formula for Binomial Coefficients.

# C(n, k) = C(n-1, k-1) + C(n-1, k)
# C(n, 0) = C(n, n) = 1


def binomialCoeffRec(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomialCoeffRec(n - 1, k - 1) + binomialCoeffRec(n - 1, k)


def binomialCoeffMemo(n, k, dp):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    if dp[n][k] == -1:
        a = binomialCoeffMemo(n - 1, k - 1, dp)
        b = binomialCoeffMemo(n - 1, k, dp)
        dp[n][k] = a + b
        return dp[n][k]

    else:
        return dp[n][k]


def binomialCoeffIter(n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(0, n + 1):
        # NOTE: see for loop range
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]


n = int(input())
k = int(input())
dp = [[-1 for i in range(k + 1)] for j in range(n + 1)]
# print(dp)
# print(binomialCoeffRec(n, k))
# print(binomialCoeffMemo(n, k, dp))
print(binomialCoeffIter(n, k))
