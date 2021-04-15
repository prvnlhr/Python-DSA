def permutationCoeff(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1

    return permutationCoeff(n - 1, k) + k * permutationCoeff(n - 1, k - 1)


def permutationCoeffMemo(n, k, dp):
    if k > n:
        return 0
    if k == 0:
        return 1
    if dp[n][k] == -1:
        a = permutationCoeffMemo(n - 1, k, dp)
        b = k * permutationCoeffMemo(n - 1, k - 1, dp)
        dp[n][k] = a + b
        return dp[n][k]
    else:
        return dp[n][k]


def permutationCoeffIter(n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):

            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + j * dp[i - 1][j - 1]
            # IMPORTANT:: for j>i P(i,j) =0
            if j < k:
                dp[i][j + 1] = 0
    return dp[n][k]


n = int(input())
k = int(input())
print(permutationCoeff(n, k))
dp = [[-1 for i in range(k + 1)] for j in range(n + 1)]
print(permutationCoeffMemo(n, k, dp))
print(permutationCoeffIter(n, k))
