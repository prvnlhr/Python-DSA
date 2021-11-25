# NOTE ::
# adjMatrix is easy to implement and use but takes a lot of memory
# adjList is bit complex to query is very space efficient
# if a graph is dense(no of edges are not very less then we can use adjMatrix),
# but if a graph is sparse graph it is better to use adjList


# FOR ADJACENCY MATRIX____
# class Graph:
#     def __init__(self, nVertices):
#         self.nVertices = nVertices
#         self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
#
#     def addEdge(self, v1, v2):
#         self.adjMatrix[v1][v2] = 1
#         self.adjMatrix[v2][v1] = 1
#
#     def printGraph(self):
#         for i in self.adjMatrix:
#             print(i)

# FOR ADJACENCY LIST____
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjList = {}
        for i in range(self.nVertices + 1):
            self.adjList[i] = []

    def addEdge(self, v1, v2):

        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)
    def printGraph(self):
        for i in self.adjList:
            print(i, "-->", self.adjList[i])


# ___Graph using adjacency Matrix__________________________________
# edgeVertices = [int(i) for i in input().strip().split()]
# V = edgeVertices[0]
# E = edgeVertices[1]
# g = Graph(V)
# for i in range(V):
#     arr = [int(i) for i in input().strip().split()]
#     v1 = int(arr[0])
#     v2 = int(arr[1])
#     print(v1, v2)
#     g.addEdge(v1, v2)
# g.printGraph()

# ___Graph using adjacency List__________________________________
V, E = [int(i) for i in input().strip().split()]
g = Graph(V)
g.printGraph()
for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)
g.printGraph()
# __________________________________________
# ______Examples
# Ex__1:
# V = 4
# E = 3
# 0 2
# 2 1
# 1 3
#
# Ex__2:
# V = 6
# E = 8
# 1 2
# 1 4
# 2 3
# 4 3
# 4 5
# 5 3
# 5 6
# 6 4
