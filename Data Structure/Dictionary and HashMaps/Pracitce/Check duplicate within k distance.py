def checkDuplicate(arr, k):
    m = {}

    for i in range(len(arr)):
        # print(m)

        if arr[i] in m:
            index = m[arr[i]]
            curr_index = i
            # print(arr[i], curr_index, index)
            if curr_index - index <= k:
                return 'true'
        else:
            m[arr[i]] = i
    return 'false'


n = int(input())
arr = [int(i) for i in input().strip().split()]
k = int(input())
print(checkDuplicate(arr, k))
