import sys


def ArrayIntersection(arr1, arr2, n, m):
    for i in range(n):
        for j in range(m):
            if (arr1[i] == arr2[j]):
                print(arr1[i], end=' ')
                arr2[j] = sys.maxsize
                break


def takeInput():
    n = int(input())
    if (n == 0):
        return list(), n
    arr = [int(i) for i in input().split()]
    return arr, n


t = int(input())

while (t > 0):
    arr1, n = takeInput()
    arr2, m = takeInput()
    ArrayIntersection(arr1, arr2, n, m)

    t = t - 1
