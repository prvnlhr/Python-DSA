def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
        print(arr)


arr = [int(i) for i in input().split()]
SelectionSort(arr)
print(arr)
