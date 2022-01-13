from ArrayTakeInputUse import *


# Naive solution T: O(N^2) ,S:O(1)
def findDuplicate(arr, n):
    for i in range(n):
        for j in range(n):
            if (i != j):
                if (arr[i] == arr[j]):
                    return arr[i]


def takeInput():
    n = int(input())
    if n == 0:
        return list(), 0
    arr = [int(i) for i in input().split()]
    return arr, n


t = int(input())

while (t > 0):
    arr, n = takeInput()
    print(findDuplicate(arr, n))
    t = t - 1
