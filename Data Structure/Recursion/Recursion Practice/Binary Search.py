def BinarySearchHelper(arr, start, end, x):
    if start > end:
        return -1
    mid = (start + end) // 2
    if (arr[mid] == x):
        return mid

    if (arr[mid] > x):
        return BinarySearchHelper(arr, start, mid - 1, x)
    else:
        return BinarySearchHelper(arr, mid + 1, end, x)


def BinarySearch(arr, x):
    start = 0
    end = len(arr) - 1
    res = BinarySearchHelper(arr, start, end, x)
    return res


arr = [int(i) for i in input().split()]
x = int(input())
print(BinarySearch(arr, x))
