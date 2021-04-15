from sys import stdin

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def isValidPosition(newx, newy, n):
    if newx >= 0 and newx < n and newy >= 0 and newy < n:
        return True


def dfs(arr, visited, x, y, n):
    visited[x][y] = True
    count = 1

    for i in range(4):
        newx = x + dir[i][0]
        newy = y + dir[i][1]
        if (isValidPosition(newx, newy, n) and arr[newx][newy] == 1 and visited[newx][newy] == False):
            count += dfs(arr, visited, newx, newy, n)
    return count


def solve(arr, n):
    visited = [[False for i in range(n)] for j in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == False and arr[i][j] == 1):
                ans = max(ans, dfs(arr, visited, i, j, n))
    return ans


n = int(input())
# n = int(stdin.readline().strip())
arr = [[int(i) for i in input().strip().split()] for j in range(n)]
# arr = [stdin.readline().strip().split() for i in range(n)]

# for i in range(n):
    # for j in range(n):
        # print(arr[i][j], end=' ')
        # print(arr[i][j] == 1, end=' ')
    # print()
print(solve(arr, n))
