import heapq as pq

def peek(heap):
    peek = pq.heappop(heap)
    pq.heappush(heap , peek)

    return peek

def isEmpty(heap):
    if len(heap)!=0:
        return False

    return True

def kLargest(li , k ):
    heap = []
    for i in range(k):
        pq.heappush(heap , li[i])

    for i in range(k , len(li)):
        if li[i]> peek(heap):
            pq.heappop(heap)
            pq.heappush(heap , li[i])

    ans = []
    while not isEmpty(heap):
        ans.append(pq.heappop(heap))
    return ans

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')



