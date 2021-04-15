def takeInput():
    n = int(input())
    if n == 0:
        return list(), 0
    arr = [int(i) for i in input().split()]
    return arr, n
