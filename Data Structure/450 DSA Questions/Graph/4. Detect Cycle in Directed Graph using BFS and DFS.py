def checkCycleHelper(adjList, visited, recursionPath, sv):
    visited[sv] = True
    recursionPath[sv] = True

    for j in adjList[sv]:
        if visited[j] == False:
            if (checkCycleHelper(adjList, visited, recursionPath, j)):
                return True
        elif recursionPath[j] == True:
            return True

    recursionPath[sv] = False
    return False


def checkCycle(adjList, nVertices):
    visited = [False for _ in range(nVertices + 1)]
    recursionPath = [False for _ in range(nVertices + 1)]

    for j in range(nVertices + 1):
        if (checkCycleHelper(adjList, visited, recursionPath, 0)):
            return True
    return False


# main method___________

V, E = [int(i) for i in input().strip().split()]
adjList = [[] for i in range(V + 1)]
for i in range(E):
    arr = [int(x) for x in input().strip().split()]
    a = int(arr[0])
    b = int(arr[1])
    adjList[a].append(b)

print(adjList)
print(checkCycle(adjList, V))
