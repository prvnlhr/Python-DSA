# Check if given undirected graph is connected or not

# If each vertex of a graph is connected to one or multiple
# vertices then the graph is called a Connected graph whereas,
# if there exists even one vertex which is not connected to any
# vertex of the graph then it is called Disconnect or not connected graph.

# APPROACH________
# Create a boolean visited [] array. Start DFS from any vertex and mark
# the visited vertices in the visited[] array. Once DFS is completed
# check the iterate the visited [] and count all the true’s.
# If this count is equal to no of vertices means all vertices are traveled
# during DFS implies graph is connected if the count is not equal to no of
# vertices implies all the vertices are not traveled means graph is not connected or disconnected.


def dfsCheckHelper(nVertices, visited, sv, adjMatrix):
    visited[sv] = True

    for i in range(nVertices):
        if (visited[i] == False and adjMatrix[sv][i] > 0):
            dfsCheckHelper(nVertices, visited, i, adjMatrix)
            visited[i] = True


def defCheck(nVertices, adjMatrix):
    visited = [False for i in range(nVertices)]
    dfsCheckHelper(nVertices, visited, 0, adjMatrix)
    print(visited)
    for j in visited:
        if j == False:
            return 'Not connected'
    return 'Connected'


# main method___________

V, E = [int(i) for i in input().strip().split()]
adjMatrix = [[0 for i in range(V)] for j in range(V)]

for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    a = int(arr[0])
    b = int(arr[1])
    adjMatrix[a][b] = 1
    adjMatrix[b][a] = 1

print(defCheck(V, adjMatrix))

# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
#
# Sample Input 2:
# 4 3
# 0 1
# 1 3
# 0 3
# Sample Output 2:
# false