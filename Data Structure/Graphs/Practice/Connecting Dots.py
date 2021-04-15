from sys import stdin

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def isValidPosition(newx, newy, n, m):
    if newx >= 0 and newx < n and newy >= 0 and newy < m:
        return True


def dfs(x, y, fromX, fromY, visited, arr, n, m):
    # Base case
    # this is the terminating step,
    # if a cycle of color is completed the it will reach at
    # the point where it start where visited will be == TRUE
    if visited[x][y]:
        return True

    visited[x][y] = True

    ans = False
    for i in range(4):
        newx = x + dir[i][0]
        newy = y + dir[i][1]
        if newx == fromX and newy == fromY:
            continue
        if isValidPosition(newx, newy, n, m) and arr[newx][newy] == arr[x][y]:
            ans |= dfs(newx, newy, x, y, visited, arr, n, m)

    # visited[x][y] = False

    return ans


def solve(arr, n, m):
    visited = [[False for i in range(m)] for j in range(n)]
    # ans = False
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                ans = dfs(i, j, -1, -1, visited, arr, n, m)
                if ans == True:
                    break
        if ans == True:
            break
    return ans


# _______________________________________________________________________
def takeInput():
    # To take fast I/O
    n, m = list(map(int, stdin.readline().strip().split()))
    arr = [stdin.readline().strip() for i in range(n)]
    return arr, n, m


# Main
arr, n, m = takeInput()
ans = solve(arr, n, m)

if (ans):
    print('true')
else:
    print('false')
