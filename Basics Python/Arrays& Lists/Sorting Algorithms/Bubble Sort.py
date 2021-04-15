def BubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        print(i)
        for j in range(length-1-i):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)


arr = [int(i) for i in input().split()]
BubbleSort(arr)
print(arr)
