from collections import defaultdict


# CONCEPT::
# Do DFS traversal on graph,
# main a parent vertex so that we know from which vertex we have come
# now for sv call DFS(sv,parent)
# if direct connection and not visited call dfs
# elif visited and direct connection and is not parent means we have cycle

def dfsCycleChecListkHelper(visited, adjList, nVertices, sv, parent):
    visited[sv] = True
    # NOTE IMP:: if adjList[sv] == [] this loop will no execute
    for j in adjList[sv]:
        # Ex..at sv == 1
        # adjList[sv] -->  adjList[1] --> [ 1 , 3 , 4]
        # in 1st iteration j --> 1 ,2nd j --> 3 , 3rd j --> 4
        if not visited[j]:
            ans = dfsCycleChecListkHelper(visited, adjList, nVertices, j, sv)
            if ans == True:
                return True
        elif j != parent:
            return True
    return False


def dfsCycleCheckList(adjList, nVertices):
    visited = [False for i in range(nVertices + 1)]
    for i in range(nVertices):
        if not visited[i]:
            ans = dfsCycleChecListkHelper(visited, adjList, nVertices, i, -1)
            if ans == True:
                return True
    return False


# ______USING ADJACENCY MATRIX_______________
def dfsCycleCheckMatHelper(visited, adjMatrix, nVertices, sv, parent):
    visited[sv] = True
    for j in range(nVertices + 1):
        # print('loop j at sv ==', sv, '-->', j)
        # if Direct connection:
        if adjMatrix[sv][j] > 0:
            # print('j', j, adjMatrix[sv][j])
            # direct connection and not visited previously explore
            if visited[j] == False:
                return dfsCycleCheckMatHelper(visited, adjMatrix, nVertices, j, sv)
            # if direct connection but visited and not parent of current node ,means cycle
            elif j != parent:
                return True
    # if no adjacent connection ,
    return False


def dfsCycleCheckMat(adjMatrix, nVertices):
    visited = [False for i in range(nVertices + 1)]
    # print(visited)
    for i in range(nVertices):
        if (visited[i] == False):
            ans = dfsCycleCheckMatHelper(visited, adjMatrix, nVertices, i, -1)
            if ans == True:
                return True
    return False


# main method___________

V, E = [int(i) for i in input().strip().split()]
# ex__1:
# V = 8 , E = 7
# 1 3
# 3 4
# 2 5
# 5 8
# 5 6
# 8 7
# 6 7
# ex__2:
# V = 2 , E = 2
# 0 1
# 1 2
# adjMatrix
adjMatrix = [[0 for i in range(V + 1)] for j in range(V + 1)]
# adjList
adjList = [[] for i in range(V + 1)]

for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    a = int(arr[0])
    b = int(arr[1])
    adjMatrix[a][b] = 1
    adjMatrix[b][a] = 1
    adjList[a].append(b)
    adjList[b].append(a)
# print(adjList)
# for i in adjMatrix:
#     print(i)

# CAUTION MAT SOLUTION DOES NOT WORK EX_ V = 5 , 1 0 ,2 0 ,0 3 ,3 4
# print(dfsCycleCheckMat(adjMatrix, V))
print(dfsCycleCheckList(adjList, V))

# Time Complexity: O(V+E).
# The program does a simple DFS Traversal of the graph which is
# represented using adjacency list. So the time complexity is O(V+E).
# Space Complexity: O(V).
# To store the visited array O(V) space is required.
