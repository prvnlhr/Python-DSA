from Implement_Graph import Graph

def getPath_helper(sv, ev, visited):
    visited[sv] = True
    # if end is reached we have path
    # we will create a new arr and append sv to it and return it
    if sv == ev:
        arr = []
        arr.append(sv)
        return arr

    for i in range(g.nVertices):
        if (visited[i] == False and g.adjMatrix[sv][i] > 0):
            ans = getPath_helper(i, ev, visited)
            if (ans != None):
                ans.append(sv)
                return ans
    return None


def hasPath(sv, ev):
    visited = [False for i in range(g.nVertices)]
    ans = getPath_helper(sv, ev, visited)
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
if res != None:
    for i in res:
        print(i, end=" ")
