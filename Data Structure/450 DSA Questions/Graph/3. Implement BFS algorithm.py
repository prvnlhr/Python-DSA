class Graph:

    def __init__(self, nVertics):
        self.nVertices = nVertics
        self.adjMatrix = [[0 for i in range(nVertics)] for j in range(nVertics)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def bfs_helper(self, visited):



    def Bfs(self):
        visited = [False for i in range(self.nVertices)]
        ans = self.bfs_helper(visited)


edgeVertices = [int(i) for i in input().strip().split()]
V = int(edgeVertices[0])
E = int(edgeVertices[1])
g = Graph(V)

for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)

g.Bfs()
