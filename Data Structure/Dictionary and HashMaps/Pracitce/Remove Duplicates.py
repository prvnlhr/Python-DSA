def removeDuplicates(arr):
    m = {}
    ans = []
    for ele in arr:
        if ele in m:
            m[ele] = m[ele] + 1
        else:
            ans.append(ele)
            m[ele] = 1
    return ans


arr = [int(i) for i in input().strip().split()]
n = arr[0]
arr = arr[1:]
ans = removeDuplicates(arr)
# print(ans)
for i in ans:
    print(i, end=" ")
