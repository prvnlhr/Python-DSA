import heapq
from collections import defaultdict


def cheapestFlights(n, flights, src, dst, k):
    INF = float('inf')
    adjList = defaultdict(list)
    stopArray = [INF] * n

    for a, b, w in flights:
        adjList[a].append((b, w))

    min_heap = []
    heapq.heappush(min_heap, (0, src, -1))

    while min_heap:
        cost, city, stops = heapq.heappop(min_heap)
        if city == dst:
            return cost
        # NOTE: WE ARE USING STOP_ARRAY TO OPTIMISE
        # CHECKING , OTHERWISE WE WILL GET TLE
        if stops == k or stops >= stopArray[city]:
            continue
        stopArray[city] = stops
        for adjCity, adjCity_cost in adjList[city]:
            heapq.heappush(min_heap, (adjCity_cost + cost, adjCity, stops + 1))

    return -1


# ____________________________________________________-

def cheapFlights2(n, flights, src, dest, k):
    adjList = defaultdict(list)

    stopsArray = [float('inf')] * n

    for v1, v2, w in flights:
        adjList[v1].append((v2, w))

    min_heap = [(0, src, -1)]

    heapq.heapify(min_heap)

    while len(min_heap) > 0:
        curr_city_cost, curr_city, curr_stop = heapq.heappop(min_heap)

        if curr_city == dest:
            return curr_city_cost

        # check if curr_stop is equal to max allowed stops or,
        # check if previous stops till curr_city is less then curr_stop
        if curr_stop == k or curr_stop >= stopsArray[curr_city]:
            continue

        stopsArray[curr_city] = curr_stop

        for adjCity, cost in adjList[curr_city]:
            src_to_curr_city_cost = curr_city_cost + cost
            heapq.heappush(min_heap, (src_to_curr_city_cost, adjCity, curr_stop + 1))


'''
5 7
[[0, 1, 1][0, 2, 5],[0, 4, 2],[1, 2, 3],[2, 3, 4],[4, 3, 8],[4, 2, 1]]
'''

# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]

n = 5
flights = [[0, 1, 1], [0, 2, 5], [0, 4, 2], [1, 2, 3], [2, 3, 4], [4, 3, 8], [4, 2, 1]]
# src_dest_k = [int(i) for i in input().strip().split()]
src = 0
dest = 3
k = 3
ans = cheapFlights2(n, flights, src, dest, k)
print(ans)
