#
# Given an array and a range [lowVal, highVal], partition the array
# around the range such that array is divided in three parts.
# 1) All elements smaller than lowVal come first.
# 2) All elements in range lowVal to highVVal come next.
# 3) All elements greater than highVVal appear in the end.
# The individual elements of three sets can appear in any order.
#
# Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}
#         lowVal = 14, highVal = 20
# Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}
#
# Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}
#        lowVal = 20, highVal = 20
# Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54}


#
# Simple solution will be to sort array using merge sort O(NlogN)
#
# Efficient solution using two pointer
# Time Complexity: O(n)
# Auxiliary Space: O(1)


def threeWayPartition(arr, low, high):
    start = 0
    end = len(arr) - 1
    i = 0
    while i < end:

        # if element is smaller then low ,swap with start and increment i and start
        if arr[i] < low:
            arr[i], arr[start] = arr[start], arr[i]
            i = i + 1
            start = start + 1
        # if element is larger then high , swap with end and decrement end
        elif arr[i] > high:
            arr[i], arr[end] = arr[end], arr[i]
            end = end - 1
        # else element is in range low to high ,increment i
        else:
            i = i + 1
    return arr


arr = [int(i) for i in input().strip().split()]
range = [int(j) for j in input().strip().split()]
ans = threeWayPartition(arr, range[0], range[1])
print(ans)
