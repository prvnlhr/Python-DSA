# There are n stairs, a person standing at the bottom wants to reach the top.
# The person can climb either 1 stair or 2 stairs at a time.
# Count the number of ways, the person can reach the top.
#
# Input: n = 1
# Output: 1
# There is only one way to climb 1 stair
#
# Input: n = 2
# Output: 2
# There are two ways: (1, 1) and (2)
#
# Input: n = 4
# Output: 5
# (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)


def staircaseRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    a = staircaseRec(n - 1)
    b = staircaseRec(n - 2)
    c = staircaseRec(n - 3)
    ans = a + b + c
    return ans


def staircaseMemo(n, dp):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    if dp[n - 1] == -1:
        a = staircaseMemo(n - 1, dp)
        dp[n - 1] = a
    else:
        a = dp[n - 1]

    if dp[n - 2] == -1:
        b = staircaseMemo(n - 2, dp)
        dp[n - 2] = b
    else:
        b = dp[n - 3]

    if dp[n - 3] == -1:
        c = staircaseMemo(n - 3, dp)
        dp[n - 3] = c
    else:
        c = dp[n - 3]

    ans = a + b + c
    return ans


n = int(input())
print(staircaseRec(n))
dp = [-1 for i in range(n + 1)]
print(staircaseMemo(n, dp))
