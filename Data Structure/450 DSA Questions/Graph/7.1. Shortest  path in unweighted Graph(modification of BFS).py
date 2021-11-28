import queue
import sys


# Time Complexity :: O(V+ E)
# Space Complexity :: O(V) + O(V) for queue and distArray


# It is BFS but slightly modified__
def shortestPathHelper(adjList, nVertices, distArray, src):
    q = queue.Queue()
    q.put(src)
    distArray[src] = 0
    while q.empty() is False:
        parent_vertex = q.get()
        dist_of_parent = distArray[parent_vertex]
        for adjNode in adjList[parent_vertex]:
            dist_of_adj_node = dist_of_parent + 1
            if dist_of_adj_node < distArray[adjNode]:
                distArray[adjNode] = dist_of_adj_node
                q.put(adjNode)
    return distArray


def shortestPath(adjList, nVertices, src, dest):
    distArray = [sys.maxsize for i in range(nVertices + 1)]
    ans = shortestPathHelper(adjList, nVertices, distArray, src)
    print(ans)


# __main driver code_____________
# Ex__
# V = 8 , E  = 11
# 8 11
# 0 1
# 0 3
# 1 3
# 1 2
# 3 4
# 4 5
# 5 6
# 2 6
# 6 7
# 6 8
# 7 8

V, E = [int(i) for i in input().strip().split()]

adjList = [[] for j in range(V + 1)]
# print(adjList)
# print('Enter Edges:')
for i in range(E):
    # print(f'Enter Edge {i + 1}')
    arr = [int(i) for i in input().strip().split()]
    a = int(arr[0])
    b = int(arr[1])
    adjList[a].append(b)
    adjList[b].append(a)
print(adjList)
# src = 0
# dest = 7

src = 2
dest = 6
# des = int(input())
shortestPath(adjList, V, src, dest)
