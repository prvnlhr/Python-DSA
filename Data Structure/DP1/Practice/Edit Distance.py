# Recursive solution : O(3^(m+n)
def editDistanceREC(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        return editDistanceREC(s1, s2, m - 1, n - 1)
    dist1 = 1 + editDistanceREC(s1, s2, m, n - 1)  # insert
    dist2 = 1 + editDistanceREC(s1, s2, m - 1, n)  # remove
    dist3 = 1 + editDistanceREC(s1, s2, m - 1, n - 1)  # replace
    return min(dist1, dist2, dist3)


# Memoization solution:: Time-->O(m*n) Space--> O(m*n)
def editDistanceMEMO(s1, s2, dp):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    m = len(s1)
    n = len(s2)

    if dp[m][n] != -1:
        return dp[m][n]

    if s1[0] == s2[0]:
        ans = editDistanceMEMO(s1[1:], s2[1:], dp)
        dp[m - 1][n] = ans
        dp[m][n] = ans

    else:

        dist2 = editDistanceMEMO(s1[1:], s2, dp)  # remove
        dp[m - 1][n] = dist2

        dist1 = editDistanceMEMO(s1, s2[1:], dp)  # insert
        dp[m][n - 1] = dist1

        dist3 = editDistanceMEMO(s1[1:], s2[1:], dp)  # replace
        dp[m - 1][n - 1] = dist3

        dp[m][n] = 1 + min(dist1, dist2, dist3)
    return dp[m][n]


s1 = input()
s2 = input()
m = len(s1)
n = len(s2)
dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]
# print(dp)
print(editDistanceREC(s1, s2, m, n))
print(editDistanceMEMO(s1, s2, dp))
