# memoization
def fibM(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n - 1] == -1:
        ans1 = fibM(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]

    if dp[n - 2] == -1:
        ans2 = fibM(n - 2, dp)
        dp[n - 2] = ans2
    else:
        ans2 = dp[n - 2]

    myAns = ans1 + ans2
    return myAns

# iterative
def fibI(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i = i + 1
    return dp[n]


n = int(input())
# dp = [-1 for i in range(n + 1)]
# ans = fib(n, dp)
ans = fibI(n)
print(ans)
