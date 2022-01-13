import heapq

def checkMaxHeap(lst):
    n = len(lst)
    for i in range(n):
        left = (2*i) + 1
        right = left + 1
        if left < n and lst[left]> lst[i]:
            return False
        if right < n and lst[right] > lst[i]:
            return False
    return True

