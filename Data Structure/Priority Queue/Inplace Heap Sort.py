def downHeapify(arr , i , n ):

    parentIndex = i
    leftchild = 2 * parentIndex + 1
    rightchild = 2 * parentIndex + 2

    while leftchild < n:
        minIndex = parentIndex
        if arr[minIndex] < arr[leftchild]:
            minIndex = leftchild
        if rightchild < n and arr[minIndex] < arr[rightchild]:
            minIndex = rightchild

        if minIndex == parentIndex:
            return
        arr[minIndex] , arr[parentIndex] = arr[parentIndex] , arr[minIndex]
        parentIndex = minIndex
        leftchild = minIndex
        leftchild = 2 * parentIndex + 1
        rightchild = 2 * parentIndex + 2

def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1 , -1 ):
        downHeapify(arr , i , n)

    for i in range(n-1 , 0 , - 1):
        arr[i] , arr[0] = arr[0] ,arr[i]
        downHeapify(arr,0,i)
    return


n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')



