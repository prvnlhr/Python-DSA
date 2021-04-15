# Partition problem is to determine whether a given set can be partitioned into two subsets
# such that the sum of elements in both subsets is the same.
# Examples:
# arr[] = {1, 5, 11, 5}
# Output: true
# The array can be partitioned as {1, 5, 5} and {11}
#
# arr[] = {1, 5, 3}
# Output: false
# The array cannot be partitioned into equal sum sets.
#
# Following are the two main steps to solve this problem:
# 1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
# 2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.
# The first step is simple. The second step is crucial, it can be solved either using
# recursion or Dynamic Programming.
#
#
# Recursive Solution
# Following is the recursive property of the second step mentioned above.
#
# Let isSubsetSum(arr, n, sum/2) be the function that returns true if
# there is a subset of arr[0..n-1] with sum equal to sum/2
#
# The isSubsetSum problem can be divided into two subproblems
#  a) isSubsetSum() without considering last element
#     (reducing n to n-1)
#  b) isSubsetSum considering the last element
#     (reducing sum/2 by arr[n-1] and n to n-1)
# If any of the above the above subproblems return true, then return true.
# isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
#                               isSubsetSum (arr, n-1, sum/2 - arr[n-1])


def partitionRec(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n - 1] > sum:
        return partitionRec(arr, n - 1, sum)
    return partitionRec(arr, n - 1, sum - arr[n - 1]) or partitionRec(arr, n - 1, sum)


def partitionMemo(arr, n, sum, dp):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if dp[n][sum] != -1:
        return dp[n][sum]
    else:
        a = partitionMemo(arr, n - 1, sum, dp)
        b = partitionMemo(arr, n - 1, sum - arr[n - 1], dp)
        ans = a or b
        dp[n][sum] = ans
        return ans


def partition(arr):
    n = len(arr)
    sum = 0
    for i in arr:
        sum = sum + i

    if sum % 2 != 0:
        return False

    else:
        dp = [[-1 for i in range((sum // 2) + 1)] for j in range(n + 1)]
        ans = partitionMemo(arr, n, sum // 2, dp)
        for i in dp:
            print(i)
        return ans
    # return partitionRec(arr, n, sum // 2)


def partitionIterDp(arr):
    n = len(arr)
    sum = 0
    for i in arr:
        sum = sum + i

    if sum % 2 != 0:
        return False

    dp = [[False for i in range((sum // 2) + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range((sum // 2) + 1):

            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    for i in range(1, n + 1):
        for j in range(1, (sum // 2) + 1):

            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                a = dp[i - 1][j - arr[i - 1]]
                b = dp[i - 1][j]

                dp[i][j] = a or b
    return dp[n][sum // 2]


arr = [int(i) for i in input().strip().split()]
print(partition(arr))
