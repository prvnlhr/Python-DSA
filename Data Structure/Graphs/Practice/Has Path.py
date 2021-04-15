## Read input as specified in the question.
## Print output as specified in the question.


class Graph:
    # __Constructor______________________________________________________________________________________________________
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]

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
    def __str__(self):
        return str(self.adjMatrix)


# Function: 98%
# def hasPathHelper(v1, v2, visited, sv):
#     if sv == v2:
#         return True
#
#     visited[sv] = True
#     for i in range(g.nVertices):
#         if g.adjMatrix[sv][i] > 0 and visited[i] == False:
#             res = hasPathHelper(v1, v2, visited, i)
#             if res == True:
#                 return True
#     return False
#
#
# def hasPath(v1, v2, visited):
#     for i in range(g.nVertices):
#         if visited[i] == False:
#             if hasPathHelper(v1, v2, visited, i):
#                 return True
#             else:
#                 return False
# 100%
def hasPath(sv, ev, visited):
    if sv == ev:
        return True

    visited[sv] = True

    for i in range(g.nVertices):
        if g.adjMatrix[sv][i] > 0 and visited[i] == False:
            visited[i] = True
            if (hasPath(i, ev, visited) == True):
                return True
    return False

# __Main______________________________________________________
li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)
edges = input().strip().split()
sv = int(edges[0])
ev = int(edges[1])
visited = [False for i in range(g.nVertices)]

res = hasPath(sv, ev, visited)
if res == True:
    print("true")
else:
    print("false")
