## Read input as specified in the question.
## Print output as specified in the question.
import heapq

# You want to buy a ticket for a well-known concert which is happening in
# your city. But the number of tickets available is limited.
# Hence the sponsors of the concert decided to sell tickets
# to customers based on some priority.
# A queue is maintained for buying the tickets and every person
# is attached with a priority (an integer, 1 being the lowest priority).
# The tickets are sold in the following manner ---

# 1. The first person (pi) in the queue requests for the ticket.
# 2. If there is another person present in the queue who has
# higher priority than pi, then ask pi to move at end of the queue without giving him the ticket.
# 3. Otherwise, give him the ticket (and don't make him stand in queue again).

# IMPORTANT INSTRUCTION IN QUESTION__
# Giving a ticket to a person takes exactly 1 minute and
# it takes no time for removing and adding a person to the queue.
# And you can assume that no new person joins the queue.
# Given a list of priorities of N persons standing in
# the queue and the index of your priority (indexing starts from 0).
# Find and return the time it will take until you get the ticket.
import queue


# Perfect solution using max_heap
# Time complexity : O(N * log N)
# Space complexity: O(N)
# STEPS:
# 1. Maintain a queue and a max_heap
# 2. In queue put index of element in lst and in max_heap all element in lst
# 3. Run a loop till max_heap does not becomes empty
# 4. now pop a element from queue, which will give us index of top element of lst
# 5. Now, compare these element with max_heap top element
# 6. there can be two conditions,
# _____if queue top element is equal,
# ________we will check if index of queue top is equal to k, then return time + 1
# _________else , heappop() and q.pop()
# __________
# _____if not equal,
# _______pop these queue element and move it to queue ending.

def buyTickets(lst, k):
    max_heap = []
    q = [int(i) for i in range(len(lst))]

    for i in lst:
        heapq.heappush(max_heap, i)

    heapq._heapify_max(max_heap)
    time = 0
    print(q, max_heap)
    while len(max_heap) != 0:
        peekIndex = q[0]
        peekElement = lst[peekIndex]
        print(peekElement, max_heap[0])
        if peekElement == max_heap[0]:
            if peekIndex == k:
                return time + 1
            else:
                time = time + 1
                q.pop(0)
                heapq._heappop_max(max_heap)

        else:
            a = q.pop(0)
            q.append(a)


# def buyTickets(lst, k):
#     max_heap = []
#     q = []
#
#     for i in lst:
#         q.append(i)
#         heapq.heappush(max_heap, i)
#     heapq._heapify_max(max_heap)
#     time = 0
#
#     while len(max_heap) != 0:
#
#         if q[0] == max_heap[0]:
#             if k == 0:
#                 return time + 1
#             else:
#                 time = time + 1
#                 q.pop(0)
#                 heapq._heappop_max(max_heap)
#                 k = k - 1
#         else:
#             a = q.pop(0)
#             if k == 0:
#                 k = len(q) - 1
#             else:
#                 k = k - 1
#     return time
#

# def buyTickets(lst, k):
#     time = 0
#     heap = []
#     q = [int(i) for i in range(len(lst))]
#     for i in lst:
#         heapq.heappush(heap, i)
#     heapq._heapify_max(heap)
#     while (len(heap)) > 0:
#         max_priority_person = heap[0]
#         curr_person_index = q[0]
#         print(lst[curr_person_index], max_priority_person)
#         if curr_person_index == k:
#             print('cond 1')
#             return time
#         if lst[curr_person_index] == max_priority_person:
#             print('cond 2')
#             time = time + 1
#             heapq.heappop(heap)
#         elif lst[curr_person_index] < max_priority_person:
#             print('cond 3')
#             a = q.pop(0)
#             print('pop', a)
#             q.append(a)
#             print(q)
#             print()
#

n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = buyTickets(lst, k)
print(ans)
