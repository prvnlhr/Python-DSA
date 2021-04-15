# Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
#
# 1. Count the number of expressions containing n pairs of parentheses which are correctly matched.
# For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
#
# 2. Count the number of possible Binary Search Trees with n keys (See this)
#
# 3. Count the number of full binary trees (A rooted binary tree is full if every
# vertex has either two children or no children) with n+1 leaves.
#
# 4.Given a number n, return the number of ways you can draw n chords in a circle
# with 2 x n points such that no 2 chords intersect.
#
# See this for more applications.
# The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

# ________________________________
# res = res + f(i) * f(n-i-1)
# --------------------------------


def nthCatalanRec(n):
    if n <= 1:
        return 1
    res = 0

    for i in range(n):
        res = res + nthCatalanRec(i) * nthCatalanRec(n - i - 1)
    return res


def nthCatalanIter(n):
    dp = [0 for i in range(n + 2)]
    # print(dp)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(0, i):
            dp[i] = dp[i] + dp[j] * dp[i - j - 1]
    return dp[n]


n = int(input())
#
for i in range(10):
    # print(nthCatalanRec(i), end=" ")
    # print()
    print(nthCatalanIter(i), end=" ")

# print(nthCatalanRec(n))
