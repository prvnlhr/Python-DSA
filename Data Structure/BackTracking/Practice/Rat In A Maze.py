def ratInMazeHelper(n, maze, sol, x, y):
    # Base case
    if x == n - 1 and y == n - 1:
        sol[x][y] = 1
        print(sol)
    # Edge cases
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or sol[x][y] == 1:
        return

    sol[x][y] = 1
    ratInMazeHelper(n, maze, sol, x + 1, y)
    ratInMazeHelper(n, maze, sol, x, y + 1)
    ratInMazeHelper(n, maze, sol, x - 1, y)
    ratInMazeHelper(n, maze, sol, x, y - 1)
    sol[x][y] = 0
    return


def ratInMaze(n, maze):
    sol = [[0 for i in range(n)] for j in range(n)]
    ratInMazeHelper(n, maze, sol, 0, 0)


n = int(input())
maze = [[int(i) for i in input().strip().split()] for x in range(n)]
ratInMaze(n, maze)
