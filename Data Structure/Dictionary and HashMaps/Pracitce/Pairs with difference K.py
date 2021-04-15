def printPairDiffK(arr, k):
    m = {}
    pairCount = 0

    for num in arr:
        if num + k in m:
            pairCount += m[num + k]
        if k != 0 and num - k in m:
            pairCount += m[num - k]

        if num in m:
            m[num] += 1
        else:
            m[num] = 1
    return pairCount


# MY sol : 100%
def printPairDiffK(arr, k):
    m = {}
    paircount = 0
    for j in range(len(arr)):
        if arr[j] in m:
            m[arr[j]] = m[arr[j]] + 1
        else:
            m[arr[j]] = 1

    for i in arr:
        if i - k in m:
            if k == 0:
                m[i - k] = m[i - k] - 1
                paircount = paircount + m[i - k]
            else:
                paircount = paircount + m[i - k]
    return paircount


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = printPairDiffK(arr, k)
print(ans)
