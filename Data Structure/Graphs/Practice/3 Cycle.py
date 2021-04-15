from sys import stdin

count = 0


def solve(adj, verticies):
    for i in range(verticies):
        for j in range(verticies):
            if adj[i][j] == 1:
                k = j
                start = i
                check = i
                check1(adj, k, start, check)

    return count // 6


def check1(adj, k, start, check):
    global count
    for i in range(verticies):
        if adj[k][i] and i != check:
            ans = checkFinal(adj, start, i)
            if ans == 1:
                count = count + 1


def checkFinal(adj, start, i):
    for j in range(verticies):
        if adj[i][j] == 1 and j == start:
            return 1
    return 0


verticies_edges = stdin.readline().strip().split(" ")
verticies = int(verticies_edges[0].strip())
edges = int(verticies_edges[1].strip())
adj = [[0 for i in range(verticies)] for j in range(verticies)]

for i in range(edges):
    u_v = stdin.readline().strip().split(" ")
    u = int(u_v[0].strip())
    v = int(u_v[1].strip())
    adj[u][v] = 1
    adj[v][u] = 1

# for i in range(verticies):
#     for j in range(verticies):
#         print(adj[i][j], end=' ')
#     print()
print(solve(adj, verticies))
