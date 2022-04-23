from collections import defaultdict


def numberOfConComp(adjList, V):
    visited = [False for _ in range(V + 1)]
    count_of_components = 0

    def DFS(vertex):
        visited[vertex] = True

        for j in adjList[vertex]:
            if not visited[j]:
                DFS(j)

    for p in range(V):
        if not visited[p]:
            DFS(p)
            count_of_components += 1
    return count_of_components


V, E = [int(x) for x in input().strip().split()]
adjList = defaultdict(list)

for _ in range(E):
    arr = [int(i) for i in input().strip().split()]
    a = arr[0]
    b = arr[1]
    adjList[a].append(b)
    adjList[b].append(a)

ans = numberOfConComp(adjList, V)
print(ans)
