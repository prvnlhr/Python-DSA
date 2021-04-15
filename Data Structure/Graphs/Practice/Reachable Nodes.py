from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
import queue


def dfs(sv, adj, visited, x):
    for i in range(verticies + 1):
        if adj[sv][i] > 0 and visited[sv][i] == False:
            visited[sv][i] = True
            x = x + 1
            dfs(i, adj, visited, x)
    return x


def count(verticies, adj):
    visited = [[False for i in range(verticies + 1)] for i in range(verticies + 1)]

    arr = []
    for i in range(1, verticies + 1):
        x = 0
        ans = dfs(i, adj, visited, x)
        arr.append(ans)

    print(arr)


#
# def reachableNodes(adj, verticies, sv):
#     arr = [1 for i in range(verticies + 1)]
#     # print(arr)
#     # for i in adj:
#     #     print(i)
#     q = queue.Queue()
#     visited = [[False for i in range(verticies + 1)] for i in range(verticies + 1)]
#
#     q.put(sv)
#     visited[sv][sv] = True
#
#     while q.empty() is False:
#         front = q.get()
#         print(front)
#         for i in range(len(arr)):
#
#             # print(i, end=' ')
#             if adj[front][i] > 0 and visited[front][i] == False:
#                 arr[front] = arr[front] + 1
#                 # print(arr)
#                 q.put(i)
#                 visited[front][i] = True
#         # print()
#     print(arr)
#     return
#
#
# def countNodes(adj, verticies):
#     for i in range(verticies):
#         reachableNodes(adj, verticies, i)
#
#
# def Helper(sv, adj, verticies):
#     for i in range(verticies):
#         if adj[sv][i] > 0:
#             Helper(i, adj, verticies)
#


# arr2 = [None]*len(arr1)
#
#
# def dfs(u, p, visited):
#     visited[u] = 1
#     x = 1
#     for i in range(len(adj[0])):
#         if adj[u][i] != p:
#             if not visited[adj[u][i]]:
#                 x = x + dfs(adj[u][i], u, visited)
#
#     return x
#
#
# def count(n, m, adj, visited):
#     sol = []
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             visited[j] = 0
#             sol.append(dfs(i, i, visited))
#     return sol


verticies_edges = stdin.readline().strip().split(" ")
verticies = int(verticies_edges[0].strip())
edges = int(verticies_edges[1].strip())
adj = [[0 for i in range(verticies + 1)] for i in range(verticies + 1)]

for i in range(edges):
    u_v = stdin.readline().strip().split(" ")
    u = int(u_v[0].strip())
    v = int(u_v[1].strip())
    adj[u][v] = 1
count(verticies, adj)
# visited = [0] * 1005
# print(len(visited))
# ans = count(verticies, edges, adj, visited)
# print(ans)
