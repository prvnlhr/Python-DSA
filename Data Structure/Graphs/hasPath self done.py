from Implement_Graph import Graph


def hasPath(sv, ev):
    end = ev
    visited = [False for i in range(g.nVertices)]
    visited[sv] = True

    for i in range(g.nVertices):
        if g.adjMatrix[sv][i] > 0 and visited[i] == False:
            visited[i] = True
            if (hasPathHelper(end, i, visited) == True):
                return True
    return False

#_Helper Function : "There is also Improved code in which no helper function is needed"
def hasPathHelper(end, sv, visited):
    if sv == end:
        return True

    visited[sv] = True
    # Just Applying Dfs concept and checking connection
    # only difference is that we will check end case if sv==ev
    for i in range(g.nVertices):
        if g.adjMatrix[sv][i] > 0 and visited[i] == False:
            res = hasPathHelper(end, i, visited)
            if res == True:
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
res = hasPath(sv, ev)
if res == True:
    print("true")
else:
    print("false")
