import queue


class Graph:
    # __Constructor______________________________________________________________________________________________________
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices+1)] for i in range(nVertices+1)]

    # __add Edge_____________________________________________________________________________________________________________
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # __remove Edge__________________________________________________________________________________________________________
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    # __Depth First Traversal________________________________________________________________________________________________
    def __dfsHelper(self, sv, visited):

        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0, visited)

    # _______________________________________________________________________________________________________________________
    #     Overwrite return type og graph object to adjMatrix
    def __str__(self):
        return str(self.adjMatrix)

    # __ Breadth First Traversal_____________________________________________________________________________________________

    def BfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True

        while (q.empty() is False):
            ver = q.get()
            # pop a vertex and print and get all edges
            print(ver, end=" ")

            for i in range(self.nVertices):
                if self.adjMatrix[ver][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def Bfs(self):
        visited = [False for i in range(self.nVertices)]

        for i in range(self.nVertices):
            if visited[i] is False:
                self.BfsHelper(i, visited)


# __Main______________________________________________________
#
li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)
for j in g.adjMatrix:
    print(j)

# # g.Bfs()
