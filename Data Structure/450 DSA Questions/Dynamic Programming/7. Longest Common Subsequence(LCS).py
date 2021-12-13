# Examples::
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


# def lcsREC(s, t, i, j):
#     if i == len(s) or j == len(t):
#         return 0
#
#     if s[i] == t[j]:
#         ans = 1 + lcsREC(s, t, i + 1, j + 1)
#         return ans
#     else:
#         a = lcsREC(s, t, i, j + 1)
#         b = lcsREC(s, t, i + 1, j)
#         ans = max(a, b)
#         return ans


def lcsREC(s, t):
    m = len(s)
    n = len(t)

    if m == 0 or n == 0:
        return 0

    if s[0] == t[0]:
        ans = 1 + lcsREC(s[1:], t[1:])
        return ans
    else:
        a = lcsREC(s[1:], t)
        b = lcsREC(s, t[1:])
        ans = max(a, b)
        return ans


def lcsMemo(s, t, i, j, dp):
    m = len(s)
    n = len(t)
    # base case
    if i == len(s) or j == len(t):
        dp[i][j] = 0
        return dp[i][j]

    if s[i] == t[j]:
        dp[i][j] = 1 + lcsMemo(s, t, i + 1, j + 1, dp)

    if dp[i][j] != -1:
        return dp[i][j]

    else:
        a = lcsMemo(s, t, i + 1, j, dp)
        b = lcsMemo(s, t, i, j + 1, dp)
        dp[i][j] = max(a, b)
        return dp[i][j]


#
# def lcsMemo(s, t, dp):
#     m = len(s)
#     n = len(t)
#     # base case
#
#     if m == 0 or n == 0:
#         dp[m][n] = 0
#         return dp[m][n]
#
#     if s[0] == t[0]:
#         dp[m][n] = 1 + lcsMemo(s[1:], t[1:], dp)
#     if dp[m][n] != -1:
#         return dp[m][n]
#
#     else:
#         a = lcsMemo(s[1:], t, dp)
#         b = lcsMemo(s, t[1:], dp)
#         dp[m][n] = max(a, b)
#         return dp[m][n]


def lcs(s, t):
    m = len(s)
    n = len(t)
    dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    # return lcsREC(s, t)
    return lcsMemo(s, t, 0, 0, dp)


s = input()
t = input()

ans = lcs(s, t)
print(ans)
