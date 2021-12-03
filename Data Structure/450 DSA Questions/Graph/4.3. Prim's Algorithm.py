import sys
from collections import defaultdict
from heapq import heappush, heapify, heappop


def minVertex(min_heap):
    min_vertex = heappop(min_heap)
    return min_vertex


def prims(adjList, V):
    # initialize visited array, parent array,weight array

    # keeps track if node already visited or not
    visited = [False for i in range(V)]

    # keeps parent of node so to trace a mst path
    parent = [-1 for i in range(V)]

    # weight to keep track of all vertex minimum weight
    weight = [sys.maxsize for i in range(V)]
    # weight of 0 vertex to 0 will be 0 at start,
    weight[0] = 0

    # To OPTIMIZE this solution we use heap to store minimum weight adjacent node
    # heappop will give a min_node
    # instead of heap we could have use a for loop to find the adjacent min_node but it
    # would have increased the time complexity.Refer prims algo using adjMatrix solution,
    # there we have use for loop.
    #
    # Initially we we put a pair in min_heap array --> [weight,vertex] --> [sys.maxsize, i]
    min_heap = [[sys.maxsize, _] for _ in range(V)]
    # now, in min_heap 0 vertex weight will be 0 at first,
    min_heap[0][0] = weight[0]
    # heapify to bring min weight vertex at top
    heapify(min_heap)
    print(min_heap)

    # now for every V-1 node..,
    # we will pop a node from min_heap, which will give min weight vertex from top
    # at very first iteration we will get [0,0]
    for i in range(V - 1):

        min_node = heappop(min_heap)
        print('min_node', min_node)
        print('min_heap after pop', min_heap)
        minNode_vertex = min_node[1]
        # for min_node in visited array mark as True,
        visited[minNode_vertex] = True
        # now for min_node , we will find all adjNode.This min_node will act as parent node
        for adjNode in adjList[minNode_vertex]:
            print('adjNode', adjList[minNode_vertex], adjNode)
            adj_node_weight = adjNode[1]
            adj_node_vertex = adjNode[0]
            # Comparing, if adjNode weight is smaller compare to weight in weight array,
            # we will update its value in weight array and push it into min_heap and also,
            # mark it in parent array.
            if visited[adj_node_vertex] == False and adj_node_weight < weight[adj_node_vertex]:
                weight[adj_node_vertex] = adj_node_weight
                parent[adj_node_vertex] = minNode_vertex
                heappush(min_heap, [weight[adj_node_vertex], adj_node_vertex])
                heapify(min_heap)
                print('min_heap if cond: ', min_heap)
                print()
    print(parent)
    # [-1, 0, 1, 2, 3, 2, 5, 6, 2]
    # printing
    # x = 0
    # for ele in parent:
    #     print(ele, " ", x)
    #     x = x + 1
    for i in range(1, V):
        if parent[i] > i:
            print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
        else:
            print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))


li = input().strip().split()
V = int(li[0])
E = int(li[1])

adjList = [[] for i in range(V)]

for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    w = int(arr[2])
    adjList[v1].append([v2, w])
    adjList[v2].append([v1, w])

# print(adjList)
a = 0
for _ in adjList:
    print(a, _)
    a = a + 1
print()
prims(adjList, V)
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
# O/P : [-1, 0, 1, 2, 3, 2, 5, 6, 2]
