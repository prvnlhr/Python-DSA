# Given a set of non-negative integers, and a value sum,
# determine if there is a subset of the given set with
# sum equal to given sum.

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output: True
# There is a subset (4, 5) with sum 9.
#
# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
# Output: False
# There is no subset that add up to 30.

# traversing array from end
def subsetSumRec(arr, sum, n):
    # if sum becomes zero we found a subset
    if sum == 0:
        return True
    # if n becomes zero and sum doest not becomes zero
    # that means we didn't find and subset
    if n == 0 and sum != 0:
        return False

    # case 1: if the last element is larger than sum, leave it::
    if arr[n - 1] > sum:
        return subsetSumRec(arr, sum, n - 1)
    # else::
    including = subsetSumRec(arr, sum - arr[n - 1], n - 1)
    excluding = subsetSumRec(arr, sum, n - 1)
    return including or excluding


def isSubsetPresentIt(arr, sum, n):
    dp = [[None for i in range(sum + 1)] for j in range(n + 1)]

    # if sum is 0 ,then answer is true,
    for i in range(n + 1):
        dp[i][0] = True
    # if sum is not 0 and arr is empty , then answer is false
    for j in range(1, sum + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]

    return dp[n][sum]


arr = [int(i) for i in input().strip().split()]
sum = int(input())
n = len(arr)
print(subsetSumRec(arr, sum, n))
print(isSubsetPresentIt(arr, sum, n))
