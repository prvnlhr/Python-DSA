from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# _Recursive:
def byteLandianRec(n):
    if n == 0 or n == 1:
        return n

    ans1 = byteLandianRec(n // 2)
    ans2 = byteLandianRec(n // 3)
    ans3 = byteLandianRec(n // 4)
    ans = ans1 + ans2 + ans3
    return max(n, ans)


# _Memoization:
def bytelandianMemo(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n] == -1:
        ans1 = bytelandianMemo(n // 2, dp)
        ans2 = bytelandianMemo(n // 3, dp)
        ans3 = bytelandianMemo(n // 4, dp)
        ans = ans1 + ans2 + ans3
        dp[n] = max(n, ans)
        return dp[n]
    else:
        return dp[n]


# Main
n = int(input())
print(byteLandianRec(n))
# dp = [-1 for i in range(n + 1)]
# print(bytelandianMemo(n, dp))
