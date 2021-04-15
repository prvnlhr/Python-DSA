from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
import queue


# 100 % self solved
def dfs(adj, visited, sv, verticies):
    visited[sv] = True
    for i in range(verticies):
        if adj[sv][i] > 0 and visited[i] == False:
            dfs(adj, visited, i, verticies)


def islands(adj, verticies):
    visited = [False for i in range(verticies)]
    count = 0

    for i in range(verticies):
        if visited[i] == False:
            count = count + 1
            dfs(adj, visited, i, verticies)
    return count


verticies_edges = stdin.readline().strip().split(" ")
verticies = int(verticies_edges[0].strip())
edges = int(verticies_edges[1].strip())
adj = [[0 for i in range(verticies)] for i in range(verticies)]

for i in range(edges):
    u_v = stdin.readline().strip().split(" ")
    u = int(u_v[0].strip())
    v = int(u_v[1].strip())
    adj[u][v] = 1
    adj[v][u] = 1

print(islands(adj, verticies))
# for i in adj:
#     print(i)
