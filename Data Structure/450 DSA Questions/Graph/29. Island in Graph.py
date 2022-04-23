def countIslands(adjMatrix):
    rows = len(adjMatrix)
    cols = len(adjMatrix[0])

    visited = [[False for m in range(cols + 1)] for n in range(rows + 1)]

    dirRows = [-1, 1, 0, 0, -1, 1, -1, 1]
    dirCols = [0, 0, -1, 1, -1, 1, 1, -1]

    count = 0

    def isSafe(posi, posj):
        print(posi, posj)
        return (posi >= 0 and posj >= 0 and posi < rows and posj < cols and not visited[posi][posj] and adjMatrix[posi][
            posj])

    def DFS(i, j):
        visited[i][j] = True
        for k in range(8):
            if isSafe(i + dirRows[k], j + dirCols[k]):
                DFS(i + dirRows[k], j + dirCols[k])

    for x in range(rows):
        for y in range(cols):
            if visited[x][y] == False and adjMatrix[x][y] == 1:
                DFS(x, y)
                count += 1

    return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

ans = countIslands(graph)
print(ans)
