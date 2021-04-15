def missingNumbers(arr, n):
    m = {}
    for ele in arr:
        m[ele] = 1

    min_num = min(m.keys())
    max_num = max(m.keys())
    # print(min_num, max_num)
    for i in range(min_num, max_num + 1):
        if i in m:
            continue
        else:
            print(i,end=" ")


n = int(input())
arr = [int(i) for i in input().strip().split()]
missingNumbers(arr, n)
