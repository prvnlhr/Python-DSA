from Implement_Graph import Graph
import queue


def BfsHelper(sv, ev, visited):
    mapp = {}
    q = queue.Queue()

    if g.adjMatrix[sv][ev] == 1 and sv == ev:
        ans = []
        ans.append(sv)
        return ans

    q.put(sv)
    visited[sv] = True

    while (q.empty() is False):
        front = q.get()
        # pop a vertex and print and explore the vertex to get all edges
        # print(front, end=" ")

        for i in range(g.nVertices):
            if g.adjMatrix[front][i] > 0 and visited[i] is False:
                mapp[i] = front
                q.put(i)

                visited[i] = True
                if i == ev:
                    ans = []
                    ans.append(ev)
                    value = mapp[ev]

                    while value != sv:
                        ans.append(value)
                        value = mapp[value]
                    ans.append(value)
                    return ans
    return []


def getPathBFS(sv, ev):
    # this function works for both connected and non connected graphs
    visited = [False for i in range(g.nVertices)]

    return BfsHelper(sv, ev, visited)


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

res = getPathBFS(sv, ev)
if len(res) != 0:
    for i in res:
        print(i, end=" ")
