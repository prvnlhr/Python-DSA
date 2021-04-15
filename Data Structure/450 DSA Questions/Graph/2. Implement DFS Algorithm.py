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

    def dfs_helper(self, visited, sv):

        visited[sv] = True
        print(sv)
        for i in range(len(self.adjMatrix)):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self.dfs_helper(visited, i)

    def dfs(self, sv):
        visited = [False for i in range(self.nVertices)]
        self.dfs_helper(visited, sv)


def getPath_dfs(start_vertex):
    g.dfs(start_vertex)


edgeVertices = [int(i) for i in input().strip().split()]
V = edgeVertices[0]
E = edgeVertices[1]
g = Graph(V)
for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    v1 = int(arr[0])
    v2 = int(arr[1])
    # print(v1, v2)
    g.addEdge(v1, v2)
print("Enter start vertex of path:")
start_vertex = int(input())
# print()
# g.printGraph()
# Printing dfs traversal path from start_vertex
getPath_dfs(start_vertex)
