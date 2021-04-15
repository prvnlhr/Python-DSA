
# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a
# given sequence such that all elements of the subsequence are sorted in increasing order.
# For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

def LISRec(arr, i, n):
    if i == n:
        return 0, 0

    including_max = 1
    for j in range(i + 1, n):
        if arr[j] >= arr[i]:
            further_including_max = LISRec(arr, i + 1, n)[0]
            including_max = max(including_max, 1 + further_including_max)
    excluding_max = LISRec(arr, i + 1, n)[1]
    overallMax = max(including_max, excluding_max)
    return including_max, overallMax


n = int(input())
arr = [int(i) for i in input().strip().split()]
ans = LISRec(arr, 0, n)[1]
print(ans)
