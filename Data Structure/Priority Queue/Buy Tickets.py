## Read input as specified in the question.
## Print output as specified in the question.
import heapq

def buyTickets(lst , k ):
    time = 0
    # print(lst)
    me = lst[k]
    n = len(lst)
    heapq._heapify_max(lst)
    while len(lst)>0 :
        # print("t" , time)
        a = heapq._heappop_max(lst)
        # print("a" ,a)
        time = time + 1
        if a == me:
            return time
    return time


n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans = buyTickets(lst , k )
print(ans)
