# No ways to make coin change problem
# example 1 : for V = 4 and S = {1,2,3},
# there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4.
#
# example 2: for V = 10 and S = {2, 5, 3, 6},
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
# So the output should be 5.
#
# example 2: for V = 5 and S = {1, 2, 5},
# there are five solutions: {2,2,1}, {2,1,1,1}, {1,1,1,1,1}.
# So the output should be 4.
# 5 = 5
# 5 = 2 + 2 + 1
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1
#
#
# _RECURSIVE:
def coinChangeREC(D, V, n):
    # __If V is 0 then there is , 1 solution (do not include any coin)
    if V == 0:
        return 1

    # __ If V is less than 0 then no solution exists
    if V < 0 or n < 0:
        return 0

    # __ If there are no coins and V is greater than 0, then no solution exist
    if (n <= 0 and V >= 1):
        return 0

    including_denominations = coinChangeREC(D, V - D[n - 1], n)
    excluding_denominations = coinChangeREC(D, V, n - 1)
    return including_denominations + excluding_denominations


# _MEMOIZATION:
def coinChangeMemo(D, V, n, dp):
    if n == 0:
        return 0
    if V == 0:
        return 1
    if dp[n][V] != -1:
        return dp[n][V]
    if D[n - 1] <= V:
        including_deno = coinChangeMemo(D, V - D[n - 1], n - 1, dp)
        excluding_deno = coinChangeMemo(D, V, n - 1, dp)
        ans = including_deno + excluding_deno
        dp[n][V] = ans
        return ans
    else:
        ans = coinChangeMemo(D, V, n - 1, dp)
        dp[n][V] = ans
        return ans


# _MEMOIZATION:
# def coinChangeMemo(D, V, n, dp):
#     if V == 0:
#         return 1
#     if V < 0 or n < 0:
#         return 0
#     if (n <= 0 and V >= 1):
#         return 0
#
#     if dp[n][V - D[n - 1]] == -1:
#         including_deno = coinChangeMemo(D, V - D[n - 1], n, dp)
#         dp[n][V - D[n - 1]] = including_deno
#     else:
#         including_deno = dp[n][V - D[n - 1]]
#
#     if dp[n - 1][V] == -1:
#         excluding_deno = coinChangeMemo(D, V, n - 1, dp)
#         dp[n - 1][V] = excluding_deno
#     else:
#         excluding_deno = dp[n - 1][V]
#
#     dp[n][V] = including_deno + excluding_deno
#     return dp[n][V]


# Main__
n = int(input())
D = [int(i) for i in input().strip().split()]
V = int(input())
dp = [[-1 for i in range(V + 1)] for j in range(n + 1)]
# print(coinChangeREC(D, V, n))
print(coinChangeMemo(D, V, n, dp))
