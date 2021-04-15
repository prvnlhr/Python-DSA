def staircaseRec(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    # return 1
    if n <= 1:
        return n
    # if n == 2:
    # return 2
    # if n == 3:
    # return 4
    ans1 = staircaseRec(n - 1)
    ans2 = staircaseRec(n - 2)
    # ans3 = staircaseRec(n - 3)
    return ans2 + ans1


def staircaseIter(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


n = int(input())
# print(staircaseRec(n))
# print(staircaseIter(n))
