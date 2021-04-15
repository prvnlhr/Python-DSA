import queue
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def colorGraphHelper(verticies, adj, sv):
    visited = [False for i in range(verticies)]
    colorMatrix = [None for i in range(verticies)]
    q = queue.Queue()
    q.put(sv)
    visited[sv] = True

    while q.empty() is False:
        front = q.get()
        colorMatrix[front] = 'blue'
        print(front)
        for i in range(verticies):
            if adj[front][i] > 0 and visited[i] == False:
                q.put(i)
                visited[i] = True
                print(colorMatrix[front], colorMatrix[i])
                if colorMatrix[i] == colorMatrix[front]:
                    return False
    return True


def colorGraph(adj, verticies):
    # print(visited)
    for i in range(verticies):
        ans = colorGraphHelper(verticies, adj, i)
        if ans == False:
            return 'NO'

    return 'Yes'
    # for i in adj:
    # print(i)


# main
verticies_edges = stdin.readline().strip().split(" ")
verticies = int(verticies_edges[0].strip())
edges = int(verticies_edges[1].strip())
adj = [[0 for i in range(verticies + 1)] for i in range(verticies + 1)]

for i in range(edges):
    u_v = stdin.readline().strip().split(" ")
    u = int(u_v[0].strip())
    v = int(u_v[1].strip())
    adj[u][v] = 1
    adj[v][u] = 1


ans = colorGraph(adj, verticies)
print(ans)
