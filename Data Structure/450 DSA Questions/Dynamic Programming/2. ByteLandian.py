# In ByteLand they have a very strange monetary system.
# Each ByteLandian gold coin has an integer number written on it.
# A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4.
# But these numbers are all rounded down (the banks have to make a profit).

# You can also sell Bytelandian coins for American dollars.
# The exchange rate is 1:1. But you can not buy Bytelandian coins.
# You have one gold coin. What is the maximum amount of American dollars you can get for it?
#
# Input --> Output:
# 12 --> 13
# 2 --> 2
# You can change 12 into 6, 4 and 3, and then change these into 6 + 4 + 3 = 13.
# If you try changing the coin 2 into 3 smaller coins, you will get 1, 0 and 0, and later you can get no more than 1 out of them.
# It is better just to change the 2 coin directly into 2.


def bytelandianRec(n):
    if n == 0 or n == 1:
        return n

    ans1 = bytelandianRec(n // 2)
    ans2 = bytelandianRec(n // 3)
    ans3 = bytelandianRec(n // 4)
    ans = ans1 + ans2 + ans3
    return max(n, ans)


def bytelandianMemo(n):
    dp = [-1] * n + 1

    if n == 0 or n == 1:
        return n

    if (dp[n] == -1):
        ans1 = bytelandianMemo(n // 2)
        ans2 = bytelandianMemo(n // 3)
        ans3 = bytelandianMemo(n // 4)
        ans = ans1 + ans2 + ans3
        dp[n] = ans
        return ans
    else:
        return dp[n]


def bytelandian(n):
    return bytelandianRec(n)


n = int(input())
ans = bytelandian(n)

print(ans)
