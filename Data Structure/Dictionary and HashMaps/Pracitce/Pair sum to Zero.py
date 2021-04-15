def paiSumTo0(arr):
    d = {}
    paircount = 0
    # for i in range(len(arr)):
    #     ele = arr[i]
    #     if not ele in d:
    #         d[ele] = 1
    #     else:
    #         d[ele] = d[ele] + 1
    for i in arr:
        d[i] = d.get(i, 0) + 1
    print(d)
    count = 0
    for i in range(len(arr)):
        x = -arr[i]
        # print(arr[i], -arr[i])
        if x in d and d[x] > 0:
            count = count + d[x]
            d[-x] = d[-x] - 1
    # print(d)
    # print(count)
    return count


def pairSumToZero(arr):
    d = {}
    count = 0
    for i in range(len(arr)):

        key = arr[i]
        # print(arr[i])
        if -key in d:
            print()
            count = count + 1
            # print(d[key])
            key = arr[i]
            d[i] = d[i] + 1
        else:
            d[key] = 1
    print(d)


n = int(input())
arr = [int(i) for i in input().strip().split()]
print(pairSumToZero(arr))
