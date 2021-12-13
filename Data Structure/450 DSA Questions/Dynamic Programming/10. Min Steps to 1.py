import sys


# Minimum steps to minimize n as per given condition
# Given a number n, count minimum steps to minimize it to 1 according to the following criteria:
# If n is divisible by 2 then we may reduce n to n/2.
# If n is divisible by 3 then you may reduce n to n/3.
# Decrement n by 1

# Input : n = 10
# Output : 3
#
# Input : 6
# Output : 2

def minSTepTo1REC(n):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if (n % 3 == 0):
        ans1 = minSTepTo1REC(n // 3)
    ans2 = sys.maxsize
    if (n % 2 == 0):
        ans2 = minSTepTo1REC(n // 2)

    ans3 = minSTepTo1REC(n - 1)
    ans = 1 + min(ans1, ans2, ans3)
    return ans


# Memeoization_______O(N)___________________________________________________________________________________________________
def minStepTo1Memo(n, dp):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    ans2 = sys.maxsize
    ans3 = sys.maxsize

    if (n % 3 == 0):
        if dp[n // 3] == -1:
            ans3 = minStepTo1Memo(n // 3, dp)
            dp[n // 3] = ans3
        else:
            ans3 = dp[n // 3]

    if (n % 2 == 0):
        if dp[n // 2] == -1:
            ans2 = minStepTo1Memo(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]

    if dp[n - 1] == -1:
        ans1 = minStepTo1Memo(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]

    return 1 + min(ans1, ans2, ans3)


# CN solution Iterstive___O(N)_______________________________________________________________________________________________
def minStepsTo1Iterative(n):
    if n == 1:
        return 0

    dp = [0 for i in range(n + 1)]
    dp[1] = 0

    ans2 = sys.maxsize
    ans3 = sys.maxsize

    for i in range(2, n + 1):

        # subtract 1
        ans1 = dp[i - 1]

        # Divisible 1
        if i % 2 == 0:
            ans2 = dp[i // 2]

        # Divisible by 3
        if i % 3 == 0:
            ans3 = dp[i // 3]

        dp[i] = 1 + min(ans1, ans2, ans3)
    return dp[n]


def minStepsTo1(n):
    dp = [-1 for i in range(n + 1)]
    return minSTepTo1REC(n)
    # return minStepTo1Memo(n, dp)
    # return minStepsTo1Iterative(n)


n = int(input())
ans = minStepsTo1(n)
print(ans)
