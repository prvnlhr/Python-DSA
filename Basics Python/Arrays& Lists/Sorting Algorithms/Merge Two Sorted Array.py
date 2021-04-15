def mergeTwoSortedArray(arr1, n, arr2, m):
    ans = (n + m) * [0]
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            ans[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            ans[k] = arr2[j]
            k = k + 1
            j = j + 1

    while i < n:
        ans[k] = arr1[i]
        k = k + 1
        i = i + 1

    while j < m:
        ans[k] = arr2[j]
        k = k + 1
        j = j + 1
    return ans


n = int(input())
arr1 = [int(i) for i in input().split()]
m = int(input())
arr2 = [int(i) for i in input().split()]

ans = mergeTwoSortedArray(arr1, n, arr2, m)
print(ans)
