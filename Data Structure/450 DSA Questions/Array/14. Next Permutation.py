def nextPermutation(arr):
    # step1: finding first decreasing element moving towards left side
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i = i - 1
    # step2: finding next largest element moving from left to right side
    if i >= 0:
        j = len(arr) - 1
        while j >= 0 and arr[j] <= arr[i]:
            j = j - 1

        # step3: swap
        arr[i], arr[j] = arr[j], arr[i]

    # step4:reversing i+1 right side elements
    k = i + 1
    l = len(arr) - 1
    while k < l:
        arr[k], arr[l] = arr[l], arr[k]
        k = k + 1
        l = l - 1
    return arr


arr = [int(i) for i in input().strip().split()]

ans = nextPermutation(arr)
print(ans)
