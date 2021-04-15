def getMinDiff(arr, n, k):
    if (n == 1):
        return 0
    arr.sort()

    ans = arr[n - 1] - arr[0]

    small = arr[n - 1] - arr[0]
    small = arr[0] + k
    big = arr[n - 1] - k

    if (small > big):
        small, big = big, small

    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k

        if subtract >= small or add <= big:
            continue

        if big - subtract <= add - small:
            small = subtract
        else:
            big = add
    return min(ans, big - small)


arr = [int(i) for i in input().strip().split()]
n = len(arr)
k = int(input())

ans = getMinDiff(arr, n, k)
print(ans)
