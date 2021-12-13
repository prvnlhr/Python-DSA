# Given an array arr[] of N integers, the task is to
# find the maximum difference between any two elements of the array.

# max diff is always between maximum number and minimum number in array.
# so the idea is basically find the max and min number.
# we can sort the array and find min and max from first and last position,
# but sort would take NlogN.
# We can solve it in O(N) time complexity using simple for loop.
import sys


def maxDiff(arr):
    max_num = ~sys.maxsize
    min_num = sys.maxsize
    for ele in arr:
        min_num = min(ele, min_num)
        max_num = max(ele, max_num)
    return max_num - min_num


arr = [int(i) for i in input().strip().split()]
ans = maxDiff(arr)
print(ans)
