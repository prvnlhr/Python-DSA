from Implement_Graph import Graph


# __Depth First Traversal________________________________________________________________________________________________
def dfsHelper(sv, nVertices, visited, adjMatrix):
    print(sv)
    visited[sv] = True
    for i in range(nVertices):
        if adjMatrix[sv][i] > 0 and visited[i] == False:
            dfsHelper(i, nVertices, visited, adjMatrix)


# __There are two dfs functions 1 and 2:
# function 1 only applicable for connected graph
# function 2 is applicable for both connected and non connected because,
# we are checking the remaining vertices from visited
# array i.e any vertex in visited is still false that means we still need to explore
# __1.
def dfs1(nVertices, adjMatrix):
    visited = [False for i in range(nVertices)]
    dfsHelper(0, nVertices, visited, adjMatrix)


# __2.
def dfs2(nVertices, adjMatrix):
    visited = [False for i in range(nVertices)]
    for i in range(g.nVertices):
        if visited[i] is False:
            dfsHelper(i, visited, adjMatrix)


# __Main_________________________________________________________________________________________________________________
li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)
adjMatrix = g.adjMatrix
#
# print adjMatrix:
# for i in adjMatrix:
#     print(i)
# print()
dfs1(V, adjMatrix)
