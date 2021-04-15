import sys
import queue


class Graph:
    # __Constructor______________________________________________________________________________________________________
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]


    # __add Edge_____________________________________________________________________________________________________________
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # _______________________________________________________________________________________________________________________
    def __str__(self):
        return str(self.adjMatrix)


def bfsHelper(nVertices, sv, adjMatrix, visited):
    q = queue.Queue()
    q.put(sv)
    visited[sv] = True

    while q.empty() is False:
        vertex = q.get()
        print(vertex, end=' ')

        for i in range(nVertices):
            if adjMatrix[vertex][i] > 0 and visited[i] is False:
                q.put(i)
                visited[i] = True


def bfs(nVertices, adjMatrix):
    visited = [False for i in range(nVertices)]
    for i in range(nVertices):
        if visited[i] is False:
            bfsHelper(nVertices, 0, adjMatrix, visited)


# _Main__
VerticesEdge = input().strip().split()
V = VerticesEdge[0]
E = VerticesEdge[1]
g = Graph(V)
for i in range(V):
    vertices = input().strip().split()
    v1 = int(vertices[0])
    v2 = int(vertices[1])
    g.addEdge(v1, v2)
adjMatrix = g.adjMatrix
bfs(V, adjMatrix)
