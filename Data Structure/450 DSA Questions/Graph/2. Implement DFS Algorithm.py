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

    # __________ This is recursive solution
    def dfs_helper(self, visited, sv):
        # 1 . Mark visited matrix at start vertex == True
        visited[sv] = True
        # print(sv)
        # 2. for sv row find all the direct edges which are not visited previously
        for i in range(len(self.adjMatrix)):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                # 3 . if found direct edge and is not visited previously,
                # call dfs_helper on that vertex as sv,
                self.dfs_helper(visited, i)

    def dfs1(self, sv):
        # creating a visited matrix for keep track of vertices which are already visited to avoid loop,
        visited = [False for i in range(self.nVertices)]
        self.dfs_helper(visited, sv)

    def dfs2(self, sv):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if (visited[i] == False):
                self.dfs_helper(visited, i)


def getPath_dfs(start_vertex):
    # __There are two dfs functions 1 and 2:
    # function 1 only applicable for connected graph
    # function 2 is applicable for both connected and non connected because,
    # we are checking the remaining vertices from visited
    # array i.e any vertex in visited is still false that means we still need to explore
    g.dfs1(start_vertex)
    # g.dfs2(start_vertex)


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

# NOTE: if start vertex is not given we can start traversing from 0
getPath_dfs(start_vertex)

# Ex__1
# V = 4
# E = 3
# 0 2
# 2 1
# 1 3
#    0  1  2  3
# 0  0  0  1  0
# 1  0  0  1  1
# 2  1  1  0  0
# 3  0  1  0  0
# O/P: 0-> 2-> ->1-> 3


# Ex__2
#    0  1  2  3  4  5  6
# 0  0  1  1  0  0  0  0
# 1  1  0  0  0  0  1  0
# 2  1  0  0  1  0  0  1
# 3  0  0  1  0  1  0  0
# 4  0  0  0  1  0  1  0
# 5  0  1  0  0  1  0  0
# 6  0  0  1  0  0  0  0
# O/P: 0-> 1-> 5 ->4-> 3-> 2-> 6
