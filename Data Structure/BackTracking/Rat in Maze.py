def ratInMaze(maze, n):
    solution = [[0 for j in range(n)] for i in range(n)]
    solveMaze(maze, solution, 0, 0, n)


def solveMaze(maze, solution, x, y, n):
    if (x == n - 1 and y == n - 1):
        solution[x][y] = 1
        printSolution(solution, n)
        print("")
        return
    if (x > n - 1 or x < 0 or y > n - 1 or y < 0) :
        return
    if (x > n - 1 or x < 0 or y > n - 1 or y < 0 or maze[x][y] == 0 or solution[x][y] == 1):
        return

    solution[x][y] = 1
    solveMaze(maze, solution, x - 1, y, n)
    solveMaze(maze, solution, x + 1, y, n)
    solveMaze(maze, solution, x, y - 1, n)
    solveMaze(maze, solution, x, y + 1, n)
    solution[x][y] = 0


def printSolution(solution, n):
    for i in range(0, n):
        for j in range(0, n):
            print(solution[i][j], end=" ")


n = int(input())
maze = n * [0]
for i in range(0, n):
    maze[i] = input().split()
    maze[i] = [int(j) for j in maze[i]]
ratInMaze(maze, n)
