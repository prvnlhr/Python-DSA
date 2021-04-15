#
# Inversion Count for an array indicates – how far (or close) the array is from being sorted.
# If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order,
# the inversion count is the maximum.
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
#
# Input: arr[] = {8, 4, 2, 1}
# Output: 6
#
# Explanation: Given array has six inversions:
# (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
#
#
# Input: arr[] = {3, 1, 2}
# Output: 2
#
# Explanation: Given array has two inversions:
# (3, 1), (3, 2)


# Naive Solution___ O(n^2)
# def countInversion(arr):
#     inv_count = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 inv_count = inv_count + 1
#

# MergeSort Technique__O(nlogn)
def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    inv_count = 0
    mid = len(arr) // 2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    inv_count += merge_sort(a1)
    inv_count += merge_sort(a2)
    inv_count += merge(a1, a2, arr)
    return inv_count


def merge(a1, a2, arr):
    i = 0
    j = 0
    k = 0
    count = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = a2[j]
            # Main trick
            count = count + (len(a1) - i)
            j = j + 1
            k = k + 1

    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1

    return count


arr = [int(i) for i in input().strip().split()]
ans = merge_sort(arr)
print(ans)
