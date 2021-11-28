import sys
from heapq import heappush, heapify, heappop


# Time Complexity :: O(V  + E)log V == VlogV
# Space Complexity :: O(V) + O(V) for pq and distArray

# heappush(min_heap, (1, 2))
# heappush(min_heap, (9, 8))
# heappush(min_heap, (4, 3))
#
# print(min_heap)
#
# heapify(min_heap)
# print(min_heap)
# a = heappop(min_heap)
# print(a)

def dijkstraHelper(adjList, distArray, src):
    # source to source distance is 0, so mark 0 at distArray[0] = 0
    distArray[src] = 0
    min_heap = []
    # now push initial src node to minHeap --> heappush(min_heap,[dist,node])
    heappush(min_heap, (0, src))

    # STEP:
    # 1. pop node from heap
    # 2. explore all adjNode of popped node
    # 3. calculate distance of adjNodes which is equal to , popped node weight + adjNode weight
    # 4. if this calculated distance is smaller then distance array distance for that adjNode, update it in distArray
    # 5. push this min_node in heap
    while len(min_heap) > 0:
        # 1.__pop node from top of min_heap
        parent_node = heappop(min_heap)
        # 2.__explore all adjNodes of parent popped node
        for adjNode in adjList[parent_node[1]]:
            # 3.__calculate the distance of adjNode from parent node,
            parent_node_weight = parent_node[0]
            adjNode_weight = adjNode[1]
            dist_of_adjNode = parent_node_weight + adjNode_weight
            curr_distArray_adjNode_dist = distArray[adjNode[0]]
            # 4.__compare distance with distArray,if smaller update in distArray,
            if dist_of_adjNode < curr_distArray_adjNode_dist:
                # update in distArray
                distArray[adjNode[0]] = dist_of_adjNode
                # 5.__if smaller also push in min_heap
                heappush(min_heap, (dist_of_adjNode, adjNode[0]))
                # heapify so that min weight node is always top of min_heap
                heapify(min_heap)

    # printing distArray
    x = 0
    for ele in distArray:
        print(x, " ", ele)
        x = x + 1


def dijkstra(adjList, nVertices, src):
    distArray = [sys.maxsize for _ in range(nVertices)]
    dijkstraHelper(adjList, distArray, src)


# Ex__1
# 9 14
# 0 1 4
# 0 7 8
# 1 2 8
# 1 7 11
# 2 3 7
# 2 8 2
# 2 5 4
# 3 4 9
# 3 5 14
# 4 5 10
# 5 6 2
# 6 7 1
# 6 8 6
# 7 8 7

# Ex_2__undirected
# 6 6
# 1 2 2
# 1 4 1
# 2 3 4
# 4 3 3
# 2 5 5
# 3 5 1


V, E = [int(i) for i in input().strip().split()]
adjList = [[] for i in range(V)]
print(adjList)
for i in range(E):
    arr = [int(j) for j in input().strip().split()]
    node1 = int(arr[0])
    node2 = int(arr[1])
    weight = int(arr[2])
    pair1 = [node2, weight]
    pair2 = [node1, weight]
    adjList[node1].append(pair1)
    adjList[node2].append(pair2)

src = int(input('Enter source vertex :'))
# for printing adjList
i = 0
for node in adjList:
    print(i, node)
    i = i + 1
dijkstra(adjList, V, src)
