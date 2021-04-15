import sys


def maxArea(height):
    l = len(height)
    i = 0
    j = l - 1
    area = 0
    while i < j:
        area = max(area, ((j - i) * min(height[i], height[j])))

        if (height[i] <= height[j]):
            i = i + 1
        if (height[i] >= height[j]):
            j = j - 1
    return area
# def maxArea(A):
#     l = 0
#     r = len(A) - 1
#     area = 0
#
#     while l < r:
#         # Calculating the max area
#         area = max(area, min(A[l],
#                              A[r]) * (r - l))
#
#         if A[l] < A[r]:
#             l += 1
#         else:
#             r -= 1
#     return area


height = [int(i) for i in input().split()]
print(maxArea(height))
