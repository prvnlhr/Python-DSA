import sys


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


def minStepTo1Memo(n, dp):
    if n == 1:
        return 0
    if dp[n] != -1:
        return dp[n]





def minStepsTo1(n):
    dp = [-1 for i in range(n + 1)]
    # return minSTepTo1REC(n)
    return minStepTo1Memo(n, dp)


n = int(input())
ans = minStepsTo1(n)
print(ans)
