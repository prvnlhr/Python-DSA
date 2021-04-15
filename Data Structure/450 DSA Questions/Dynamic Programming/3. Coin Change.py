# No ways to make coin change problem
# example 1 :for N = 4 and S = {1,2,3},
# there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4.
# example 2: for N = 10 and S = {2, 5, 3, 6},
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
# So the output should be 5.

# _RECURSIVE:
# def coinChangeREC(D, V, n):
#     if V == 0:
#         return 1
#     if V < 0 or n < 0:
#         return 0
#     if (n <= 0 and V >= 1):
#         return 0
#     including_deno = coinChangeREC(D, V - D[n - 1], n)
#     excluding_deno = coinChangeREC(D, V, n - 1)
#     return including_deno + excluding_deno

# _MEMOIZATION:
def coinChangeMemo(D, V, n, dp):
    if V == 0:
        return 1
    if V < 0 or n < 0:
        return 0
    if (n <= 0 and V >= 1):
        return 0

    if dp[n][V - D[n - 1]] == -1:
        including_deno = coinChangeMemo(D, V - D[n - 1], n, dp)
        dp[n][V - D[n - 1]] = including_deno
    else:
        including_deno = dp[n][V - D[n - 1]]

    if dp[n - 1][V] == -1:
        excluding_deno = coinChangeMemo(D, V, n - 1, dp)
        dp[n - 1][V] = excluding_deno
    else:
        excluding_deno = dp[n - 1][V]

    dp[n][V] = including_deno + excluding_deno
    return dp[n][V]


# Main
n = int(input())
D = [int(i) for i in input().strip().split()]
V = int(input())
dp = [[-1 for i in range(V + 1)] for j in range(n + 1)]
# print(coinChangeREC(D, V, n))
print(coinChangeMemo(D, V, n, dp))
