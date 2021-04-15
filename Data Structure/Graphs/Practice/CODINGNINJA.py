from sys import stdin

# and visited[i][j] == 0
# and  and i + 1 < n and j + 1 < m
dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def isValidPosition(newx, newy, n, m):
    if newx >= 0 and newx < n and newy >= 0 and newy < m:
        return True


def dfs(arr, visited, x, y, n, m, str, index):
    if index == 11:
        return 1

    visited[x][y] = True
    found = 0

    for i in range(8):
        newx = x + dir[i][0]
        newy = y + dir[i][1]
        if isValidPosition(newx, newy, n, m) and visited[newx][newy] == False and arr[newx][newy] == str[index]:
            found |= dfs(arr, visited, newx, newy, n, m, str, index + 1)

    visited[x][y] = False

    return found


def solve(arr, n, m):
    str = ['C', 'O', 'D', 'I', 'N', 'G', 'N', 'I', 'N', 'J', 'A']
    found = 0
    visited = [[False for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'C':
                found = dfs(arr, visited, i, j, n, m, str, 1)

                if found != 0:
                    break

        if found != 0:
            break

    return found


rowCol = input().strip().split()
n = int(rowCol[0])
m = int(rowCol[1])

arr = [stdin.readline().strip() for i in range(n)]
print(solve(arr, n, m))
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j], end=' ')
#     print()
