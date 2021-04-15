## Read input as specified in the question.
## Print output as specified in the question.

import sys


class Graph:
    # __Constructor______________________________________________________________________________________________________
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]

    # __add Edge_____________________________________________________________________________________________________________
    def addEdge(self, v1, v2, W):
        self.adjMatrix[v1][v2] = W
        self.adjMatrix[v2][v1] = W

    # __remove Edge__________________________________________________________________________________________________________
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def minvertex(self, visited, weight):
        minVertex = -1
        for i in range(self.nVertices):
            if (visited[i] is False and (minVertex == -1 or (weight[minVertex] > weight[i]))):
                minVertex = i
        return minVertex

    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]

        for i in range(self.nVertices - 1):
            minVertex = self.minvertex(visited, weight)
            visited[minVertex] = True
            for j in range(self.nVertices):
                if (self.adjMatrix[minVertex][j] > 0 and visited[j] is False):
                    if (weight[j] > self.adjMatrix[minVertex][j]):
                        weight[j] = self.adjMatrix[minVertex][j]
                        parent[j] = minVertex

        for i in range(1, self.nVertices):
            if parent[i] > i:
                print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))


li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    w = int(arr[2])
    g.addEdge(v1, v2, w)

g.prims()
