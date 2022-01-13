def kthLargest(lst , k):
    minHeap = lst[:k]
    heapq.heapify(minHeap)
    n = len(lst)
    for i in range(k , n):
        if lst[i] > minHeap[0]:
            heapq.heapreplace(minHeap , lst[i])
    return minHeap[0]
