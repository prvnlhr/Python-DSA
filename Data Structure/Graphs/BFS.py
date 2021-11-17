import queue

from Implement_Graph import Graph

# __ Breadth First Traversal_____________________________________________________________________________________________
def BfsHelper(sv, nVertices, visited, adjMatrix):
    q = queue.Queue()
    q.put(sv)
    visited[sv] = True
    while (q.empty() is False):
        ver = q.get() 
        # pop a vertex and print and get all edges97
        print(ver, end=" ")
        for i in range(nVertices):
            if adjMatrix[ver][i] > 0 and visited[i] is False:
                q.put(i)
                visited[i] = True

def Bfs(nVertices, adjMatrix):
    # this function works for both connected and non connected graphs
    visited = [False for i in range(nVertices)]
    for i in range(nVertices):
        if visited[i] is False:
            BfsHelper(i, nVertices, visited, adjMatrix)


# __Main________________________________________________________________________________________________________________
li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)
adjMatrix = g.adjMatix
Bfs(V, adjMatrix)
