path = []


def searchMazeHelper(maze, sol, n, i, j):
    # 1. Destination reached Base case:
    if (i == n - 1 and j == n - 1):
        sol[i][j] = 1
        print(sol)
        return
        # 2. Not a valid position Edge case:
    if (i >= n or i < 0 or j >= n or j < 0 or sol[i][j] == 1 or maze[i][j] == 0):
        return

    sol[i][j] = 1

    # explore a  possible direction
    searchMazeHelper(maze, sol, n, i - 1, j)
    searchMazeHelper(maze, sol, n, i + 1, j)
    searchMazeHelper(maze, sol, n, i, j + 1)
    searchMazeHelper(maze, sol, n, i, j - 1)
    sol[i][j] = 0
    return


def searchMaze(maze, n):
    sol = [[0 for i in range(n)] for i in range(n)]
    searchMazeHelper(maze, sol, n, 0, 0)


n = int(input())
maze = [[int(i) for i in input().strip().split()] for x in range(n)]
searchMaze(maze, n)
