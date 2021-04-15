def FindTriplet(arr, x):
    arr1 = sorted(arr)
    l = len(arr1)
    for i in range(0, l - 1):
        st = i + 1
        end = l - 1
        val = x - arr1[i]
        while st < end:
            if (arr1[st] + arr[end] > val):
                end -= 1
            elif (arr1[st] + arr1[end] < val):
                st += 1
            else:
                count1 = 0
                count2 = 0
                for ptr in range(st, end):
                    if (arr1[ptr] == arr1[st]):
                        count1 += 1
                    else:
                        break
                for ptr in range(end, st, -1):
                    if (arr1[ptr] == arr1[end]):
                        count2 += 1
                    else:
                        break
                comb = count2 * count1
                if (arr1[st] == arr1[end]):
                    comb = ((end - st + 1) * (end - st)) // 2
                for k in range(0, comb):
                    print(arr1[i], end=" ")
                    print(arr1[st], end=" ")
                    print(arr1[end])
                st += 1
                end = end - count2


n = int(input())
arr = [int(y) for y in input().strip().split()]
x = int(input())
FindTriplet(arr, x)
