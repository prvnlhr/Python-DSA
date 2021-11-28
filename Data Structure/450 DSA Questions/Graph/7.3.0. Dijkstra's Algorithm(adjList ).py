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
    distArray[src] = 0
    min_heap = []
    heappush(min_heap, (0, src))
    while len(min_heap) > 0:
        parent_node = heappop(min_heap)
        print('parent_node -->', parent_node)
        for adjNode in adjList[parent_node[1]]:
            parent_node_weight = parent_node[0]
            adjNode_weight = adjNode[1]
            dist_of_adjNode = parent_node_weight + adjNode_weight
            curr_distArray_adjNode_dist = distArray[adjNode[0]]
            print('parentNode :', parent_node)
            print('adjNode :', adjNode)
            print('adjNode_weight:', adjNode_weight, 'parent_node_weight', parent_node_weight)
            print('curr_distArray_adjNode_dist : ', curr_distArray_adjNode_dist, 'dist_of_adjNode', dist_of_adjNode)
            if dist_of_adjNode < curr_distArray_adjNode_dist:
                distArray[adjNode[0]] = dist_of_adjNode
                heappush(min_heap, (dist_of_adjNode, adjNode[0]))
                heapify(min_heap)
                print(min_heap)
                print(distArray)
    print(distArray)
    f = 0
    for ele in distArray:
        print(f, " ", ele)
        f = f + 1


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
