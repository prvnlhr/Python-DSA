# def maxSumSubArray(arr, size):
#     max = 0
#     sum = 0
#
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#         if sum < 0:
#             sum = 0
#         elif (sum > max):
#             max = sum
#     return max
#

# works for all negative elements in array

def maxSumSubArray(arr, size):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, size):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


arr = [int(i) for i in input().strip().split()]

ans = maxSumSubArray(arr, len(arr))
print(ans)
