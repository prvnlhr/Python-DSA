class Graph:

    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def printGraph(self):
        for i in self.adjMatrix:
            print(i)


edgeVertices = [int(i) for i in input().strip().split()]
V = edgeVertices[0]
E = edgeVertices[1]
g = Graph(V)
for i in range(V):
    arr = [int(i) for i in input().strip().split()]
    v1 = int(arr[0])
    v2 = int(arr[1])
    print(v1, v2)
    g.addEdge(v1, v2)
g.printGraph()
