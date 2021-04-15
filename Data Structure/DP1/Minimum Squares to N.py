import math, sys

# Recursive______________________________
def minSquares(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        currAns = 1 + minSquares(n - (i ** 2))
        ans = min(ans, currAns)
    return ans


# Memoization____________________________
def minSquaresM(n):
    dp = [-1 for i in range(n + 1)]
    return minSquaresMHelper(n, dp)


def minSquaresMHelper(n, dp):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        if dp[n - (i ** 2)] == -1:
            currAns = 1 + minSquaresMHelper((n - (i ** 2)), dp)
            dp[n - (i ** 2)] = currAns
        else:
            currAns = dp[n - (i ** 2)]
        ans = min(ans, currAns)
    return ans

# Iterative______________________________________
def minSquaresI(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1, root + 1):
            currAns = 1 + dp[i - (j ** 2)]
            ans = min(ans, currAns)
        dp[i] = ans
    return dp[n]


# Driver function_________________________________
n = int(input())
ans = minSquaresM(n)
print(ans)
