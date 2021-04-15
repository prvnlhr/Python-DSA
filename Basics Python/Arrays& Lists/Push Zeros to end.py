def pushZerosToEnd(arr):
    n = len(arr)
    for i in range(n):
        print("i" , i)
        if (arr[i] == 0):
            for j in range(i + 1, n):
                if (arr[j] != 0):
                    arr[i], arr[j] = arr[j], arr[i]
                    break
                    print(arr)


arr = [int(i) for i in input().split()]

pushZerosToEnd(arr)
print(arr)
