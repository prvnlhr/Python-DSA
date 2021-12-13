import sys


# Recursive_____________________________________________________________________________________________________________
def minstepsto1R(n):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if n % 3 == 0:
        ans1 = minstepsto1R(n // 3)
    ans2 = sys.maxsize
    if n % 2 == 0:
        ans2 = minstepsto1R(n // 2)

    ans3 = minstepsto1R(n - 1)
    ans = 1 + min(ans1, ans2, ans3)
    return ans


# Memeoization_______O(N)___________________________________________________________________________________________________
def minStepsTo1M(n):
    dp = [-1 for i in range(n + 1)]
    return minStepsM(n, dp)


def minStepsM(n, dp):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    ans2 = sys.maxsize
    ans3 = sys.maxsize

    if (n % 3 == 0):
        if dp[n // 3] == -1:
            ans3 = minStepsM(n // 3, dp)
            dp[n // 3] = ans3
        else:
            ans3 = dp[n // 3]

    if (n % 2 == 0):
        if dp[n // 2] == -1:
            ans2 = minStepsM(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]

    if dp[n - 1] == -1:
        ans1 = minStepsM(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]

    return 1 + min(ans1, ans2, ans3)


# Iterative DP__________________________________________________________________________________________________________
def minStepsIterSol1(n):
    dp = [-1 for i in range(n + 1)]
    dp[1] = 0
    dp[0] = 0

    for i in range(2, n + 1):

        if dp[i] == -1:
            ans1 = dp[i - 1]

        if i % 2 == 0:
            x = i // 2
            if dp[i // 2] == -1:
                ans2 = 1 + dp[x // 2]
            else:
                ans2 = dp[i // 2]
        else:
            ans2 = sys.maxsize

        if i % 3 == 0:
            y = i // 3
            if dp[i // 3] == -1:
                ans2 = 1 + dp[y // 3]
            else:
                ans3 = dp[i // 3]
        else:
            ans3 = sys.maxsize

        ans = 1 + min(ans1, ans2, ans3)
        dp[i] = ans
    return dp[n]


# CN solution Iterstive___O(N)_______________________________________________________________________________________________
def minStepsTo1Iterative(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 0
    bigNum = sys.maxsize

    for i in range(2, n + 1):

        ans1 = dp[i - 1]

        if i % 2 == 0:
            ans2 = dp[i // 2]
        else:
            ans2 = bigNum

        if i % 3 == 0:
            ans3 = dp[i // 3]
        else:
            ans3 = bigNum

        dp[i] = 1 + min(ans1, ans2, ans3)
    return dp[n]


# Main____________
n = int(input())
print(minstepsto1R(n))
print(minStepsTo1M(n))
print(minStepsTo1Iterative(n))

# n = int(input())
# ans = minStepsTo1DP(n)
# print(ans)
