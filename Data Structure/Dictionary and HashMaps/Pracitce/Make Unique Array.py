def makeUniqueArray(arr):
    m = {}
    count = 0
    for ele in arr:
        if ele in m:
            count = count + 1
            m[ele] = m[ele] + 1
        else:
            m[ele] = 1
    return count


n = int(input())
arr = [int(i) for i in input().strip().split()]
print(makeUniqueArray(arr))
