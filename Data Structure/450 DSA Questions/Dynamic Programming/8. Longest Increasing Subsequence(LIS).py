import sys


# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a
# given sequence such that all elements of the subsequence are sorted in increasing order.
# For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
#
# Input: arr[] = {3, 10, 2, 1, 20}
# Output: Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20
#
# Input: arr[] = {3, 2}
# Output: Length of LIS = 1
# The longest increasing subsequences are {3} and {2}
#
# Input: arr[] = {50, 3, 10, 7, 40, 80}
# Output: Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}


# LEETCODE BRUTE FORCE SOLUTION::

def lisREC(arr, prev, currpos):
    if currpos == len(arr):
        return 0
    including = 0
    if prev < 0 or arr[currpos] > arr[prev]:
        including = 1 + lisREC(arr, currpos, currpos + 1)
    not_including = lisREC(arr, prev, currpos + 1)
    return max(including, not_including)


def lisMemo(arr, prev, currpos, dp):
    if currpos == len(arr):
        return 0
    if dp[prev + 1][currpos] != -1:
        return dp[prev + 1][currpos]
    including = 0
    if prev < 0 or arr[currpos] > arr[prev]:
        including = 1 + lisMemo(arr, currpos, currpos + 1, dp)

    not_including = lisMemo(arr, prev, currpos + 1, dp)
    dp[prev + 1][currpos] = max(including, not_including)
    return dp[prev + 1][currpos]


#

def lis(arr):
    n = len(arr)
    # return lisREC(arr, -1, 0)
    dp = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    return lisMemo(arr, -1, 0, dp)


arr = [int(i) for i in input().strip().split()]
print(lis(arr))
