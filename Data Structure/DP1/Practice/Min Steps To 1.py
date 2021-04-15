import sys


# Given a number n, count minimum steps to minimize it to 1 according to the following criteria:
# If n is divisible by 2 then we may reduce n to n/2.
# If n is divisible by 3 then you may reduce n to n/3.
# Decrement n by 1.
#
# Input : n = 10
# Output : 3
#
# Input : 6
# Output : 2


# ___________________________________________________________________
def minStepTo1Rec(n):
    if n == 1:
        return 0
    ans3 = sys.maxsize
    if n % 3 == 0:
        ans3 = minStepTo1Rec(n // 3)
    ans2 = sys.maxsize
    if n % 2 == 0:
        ans2 = minStepTo1Rec(n // 2)

    ans1 = minStepTo1Rec(n - 1)
    ans = 1 + min(ans1, ans2, ans3)
    return ans


# ___________________________________________________________________
def minStepsTo1Mem(n, dp):
    if n == 1:
        return 0
    ans3 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans3 = minStepsTo1Mem(n // 3, dp)
            dp[n // 3] = ans3
        else:
            ans3 = dp[n // 3]
    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minStepsTo1Mem(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]
    if dp[n - 1] == -1:
        ans1 = minStepsTo1Mem(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]
    return 1 + min(ans3, ans2, ans1)


# ___________________________________________________________________
def minStepsTo1Iter(n, dp):
    dp[0] = 0
    dp[1] = 0

    for i in range(2, n + 1):

        ans1 = sys.maxsize
        ans2 = sys.maxsize
        ans3 = sys.maxsize

        ans1 = dp[i - 1]

        if i % 2 == 0:
            ans2 = dp[i // 2]
        if i % 3 == 0:
            ans3 = dp[i // 3]

        ans = 1 + min(ans1, ans2, ans3)
        dp[i] = ans

    return dp[n]


# ___________________________________________________________________
n = int(input())
dp = [-1 for i in range(n + 1)]
# print(minStepTo1Rec(n))
print(minStepsTo1Mem(n, dp))
# print(minStepsTo1Iter(n, dp))
