import sys

MIN_VALUE = -2147483648


def secondLargest(arr, n):
    if (n == 0):
        return MIN_VALUE
    largest = arr[0]
    secondLargest = MIN_VALUE
    print(sys.maxsize)
    print(~(sys.maxsize))
    for i in range(n):
        if (arr[i] > largest):
            largest = arr[i]
            secondLargest = largest
        if (arr[i] > secondLargest and arr[i] != largest):
            secondLargest = arr[i]
    return secondLargest


n = int(input())
arr = [int(i) for i in input().split()]
ans = secondLargest(arr, n)
print(ans)
