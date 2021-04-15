def MissingNumber(arr):
    arr1 = sorted(arr)
    l = len(arr1)
    for i in range(l):
        if arr1[i] == arr1[i+1]:
            return arr1[i]


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
ans = MissingNumber(arr)
print(ans)
