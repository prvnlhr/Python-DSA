# Given an array arr[] of integers, find out the maximum
# difference between any two elements such that larger element
# appears after the smaller number.


# Input : arr = {2, 3, 10, 6, 4, 8, 1}
# Output : 8
# Explanation : The maximum difference is between 10 and 2.
#
# Input : arr = {7, 9, 5, 6, 3, 2}
# Output : 2
# Explanation : The maximum difference is between 9 and 7.


# Naive Solution Time Complexity : O(n^2) ___

def maxDiff(arr):
    max_diff = arr[1] - arr[0]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            curr_diff = arr[j] - arr[i]
            max_diff = max(max_diff, curr_diff)
    return max_diff


# Optimize Solution Time Complexity : O(N) ___
def maxDiffOptimize(arr):
    max_diff = arr[1] - arr[0]
    min_ele_so_far = arr[0]

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_ele_so_far)
        min_ele_so_far = min(min_ele_so_far, arr[i])
    return max_diff


arr = [int(i) for i in input().strip().split()]
ans1 = maxDiff(arr)
print(ans1)
ans2 = maxDiffOptimize(arr)
print(ans2)
