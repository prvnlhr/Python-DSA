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

    def getMinvertex(self, visited, weight):
        minVertex = -1
        for i in range(self.nVertices):
            if (visited[i] is False and (minVertex == -1 or (weight[i] < weight[minVertex]))):
                minVertex = i
        return minVertex

    def dijkstra(self):
        visited = [False for i in range(self.nVertices)]
        dist = [sys.maxsize for i in range(self.nVertices)]
        dist[0] = 0

        for i in range(self.nVertices - 1):
            minVertex = self.getMinvertex(visited, dist)
            visited[minVertex] = True

            for j in range(self.nVertices):
                if (self.adjMatrix[minVertex][j] > 0 and visited[j] is False):
                    if (dist[j] > dist[minVertex] + self.adjMatrix[minVertex][j]):
                        dist[j] = dist[minVertex] + self.adjMatrix[minVertex][j]
        for i in range(self.nVertices):
            print(str(i) + " " + str(dist[i]))


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

g.dijkstra()
