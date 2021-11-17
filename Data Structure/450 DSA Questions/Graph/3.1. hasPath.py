from Implement_Graph import Graph

pathArr = []
def hasPath_helper(sv, ev, visited):
    visited[sv] = True
    if sv == ev:
        return True

    for i in range(g.nVertices):
        if (visited[i] == False and g.adjMatrix[sv][i] > 0):
            return hasPath_helper(i, ev, visited)


def hasPath(sv, ev):
    visited = [False for i in range(g.nVertices)]
    ans = hasPath_helper(sv, ev, visited)
    return ans


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
