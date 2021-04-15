from Implement_Graph import Graph
#__"Improved code in which there is no Helper function"__
#__hasPath Function_____________________________________________________________________________________________________
def hasPath(sv, ev, visited):
    if sv == ev:
        return True

    visited[sv] = True
    # Just Applying Dfs concept and checking connection
    # only difference is that we will check end case if sv==ev (above)
    for i in range(g.nVertices):
        if g.adjMatrix[sv][i] > 0 and visited[i] == False:
            visited[i] = True
            if (hasPath(i, ev, visited) == True):
                return True
    return False


# __Main________________________________________________________________________________________________________________
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

res = hasPath(sv, ev ,visited)
if res == True:
    print("true")
else:
    print("false")
