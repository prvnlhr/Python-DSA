#
# Given an array of integers where each element represents the max number
# of steps that can be made forward from that element. Write a function to return
# the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, they cannot move through that element. If the end isn’t reachable, return -1


# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 9 -> 9)
# Explanation: Jump from 1st element
# to 2nd element as there is only 1 step,
# now there are three options 5, 8 or 9.
# If 8 or 9 is chosen then the end node 9
# can be reached. So 3 jumps are made.
# The first element is 1, so can only go to 3. The second element is 3,
# so can make at most 3 steps eg to 5 or 8 or 9

# Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# Output: 10
# Explanation: In every step a jump
# is needed so the count of jumps is 10.


import sys


# Naive recursive solution
# __O(N * N)
def countMinimumSteps(arr, low, high):
    if (low == high):
        return 0
    if arr[low] == 0:
        return float('inf')
    min = float('inf')
    for i in range(low + 1, high + 1):
        if i < low + arr[low] + 1:
            jumps = countMinimumSteps(arr, i, high)
            if jumps != float('inf') and jumps + 1 < min:
                min = jumps + 1
    return min


# DP Solution
# __O(N ^ 2)
def countMinimumSteps(arr, n):
    jumps = [0 for i in range(len(arr))]

    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = sys.maxsize
        for j in range(0, i):
            if i <= j + arr[j] and jumps[j] != sys.maxsize:
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


# Optimize solution
# O(N)
# Implementation:
# Variables to be used:
#
# 1__. maxReach The variable maxReach stores at all
# time the maximal reachable index in the array.
# 2__. jump jump stores the amount of jumps necessary
# to reach the maximal reachable position. It also
# indicates the current jump we are making in the array.
# 3__. step The variable step stores the number of steps we
# can still take in the current jump ‘jump’ (and is initialized with value at index 0, i.e. initial number of steps)

def countMinimumSteps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    maxReach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n):
        if i == n - 1:
            return jump

        maxReach = max(maxReach, i + arr[i])
        step = step - 1

        if step == 0:
            jump = jump + 1

            if i >= maxReach:
                return -1

            step = maxReach - i
    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)

# print(countMinimumSteps(arr, 0, size - 1))
# print(countMinimumSteps(arr, size))
print(countMinimumSteps(arr))
