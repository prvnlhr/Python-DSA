def fib(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n - 1] == -1:
        ans1 = fib(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]

    if dp[n - 2] == -1:
        ans2 = fib(n - 2, dp)
        dp[n - 2] = ans2
    else:
        ans2 = dp[n - 2]

    myAns = ans1 + ans2
    return myAns


import time
n = int(input())
dp = [-1 for i in range(n + 1)]
start = time.time()
ans = fib(n, dp)
end = time.time()
print(ans , end - start)
