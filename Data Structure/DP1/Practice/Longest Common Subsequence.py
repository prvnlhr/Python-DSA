# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

def lcsDP(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    # return lcsREC(s1, s2, 0, 0)
    return lcsM(s1, s2, 0, 0, dp)
    # return lcsIterative(s1, s2)


def lcsREC(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        ans = 1 + lcsREC(s1, s2, i + 1, j + 1)
    else:
        a = lcsREC(s1, s2, i, j + 1)
        b = lcsREC(s1, s2, i + 1, j)
        ans = max(a, b)
    return ans


# Memoization___________________________________________________________________________________________________________
def lcsM(s1, s2, i, j, dp):
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        if dp[i + 1][j + 1] == -1:
            Smallans = 1 + lcsM(s1, s2, i + 1, j + 1, dp)
            dp[i + 1][j + 1] = Smallans
            ans = 1 + Smallans
        else:
            ans = 1 + dp[i + 1][j + 1]
    else:
        if dp[i][j + 1] == -1:
            a = lcsM(s1, s2, i, j + 1, dp)
            dp[i][j + 1] = a
        else:
            a = dp[i][j + 1]

        if dp[i + 1][j] == -1:
            b = lcsM(s1, s2, i + 1, j, dp)
            dp[i + 1][j] = b
        else:
            b = dp[i + 1][j]

        ans = max(a, b)
    return ans


# Iterative_____________________________________________________________________________________________________________
def lcsIterative(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):

            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]

            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


s1 = input().strip()
s2 = input().strip()
print(lcsDP(s1, s2))
