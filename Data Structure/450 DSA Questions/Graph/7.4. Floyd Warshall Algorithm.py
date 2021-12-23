import sys

INF = sys.maxsize


# Time Complexity: O(V^3)

def flyodWrashall(adjMatrix, V):
    # initialize dist_array and copy all element of adjMatrix to dist_array
    dist_matrix = [[0 for _ in range(V)] for _ in range(V)]
    for row in range(V):
        for col in range(V):
            # print(row, col, adjMatrix[row][col])
            dist_matrix[row][col] = adjMatrix[row][col]

    for ele in dist_matrix:
        print(ele)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                # relaxing step::
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    for ele in dist_matrix:
        print(ele)


# Ex. 1 __
# 4 4
# 0 1 5
# 0 3 10
# 1 2 3
# 2 3 1
V, E = [int(i) for i in input().strip().split()]

# NOTE: Floyd warshall algo works only on adjMatrix.

# initialize adjMatrix with infinite value except i = j,where it would be 0
adjMatrix = [[INF if i != j else 0 for j in range(V)] for i in range(V)]

for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    a = int(arr[0])
    b = int(arr[1])
    w = int(arr[2])
    adjMatrix[a][b] = w
# print(adjMatrix)
# for i in adjMatrix:
# print(i)
flyodWrashall(adjMatrix, V)
