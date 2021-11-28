# def canFinishHelper(numCourses, visited, sv, adjMatrix):
#     visited[sv] = True
#
#     for i in range(numCourses):
#         if (adjMatrix[sv][i] > 0 and visited[i] == False):
#             ans = canFinishHelper(numCourses, visited, i, adjMatrix)
#             if (ans == True):
#                 return True
#     return False
#
#
# def canFinish(numCourses, prerequisites):
#     g = Graph(numCourses)
#     print(g.adjMatrix)
#     for i in prerequisites:
#         g.addEdge(i[0], i[1])
#         # print(i[0], i[1])
#     print(g.adjMatrix)
#     visited = [False for i in range(numCourses)]
#     for i in range(numCourses):
#         canFinishHelper(numCourses, visited, i, g.adjMatrix, i)
#     # print(visited)
#     # for i in range(n):
#     #     if (visited[i] == False):
#     #         res = canFinishHelper(prerequisites, n, m, visited, 0)
#     #         if res == False:
#     #             return 'No'
#     # return 'Yes'
#
#
# # _____Coding Ninjas Solution______________________________________
# '''
#     Time Complexity: O(N + M)
#     Space Complexity: O(N)
#
#     where N is the number of vertices and
#     M is the number of edges in the graph.
# '''
# def isCycle(i, graph, visited, recursionPath):

#     visited[i] = True
#     recursionPath[i] = True


#     for j in graph[i]:
#         if visited[j] == False:
#             if isCycle(j, graph, visited, recursionPath):
#                 return True
#         elif recursionPath[j] ==True:
#             return True


#     recursionPath[i] = False
#     return False
#


# def canFinish(prerequisites, n, m):
#     graph = [[] for i in range(n + 1)]
#     for i in range(m):
#         graph[prerequisites[i][1]].append(prerequisites[i][0])
#     visited = [False] * (n + 1)
#     recursionPath = [False] * (n + 1)
#     for i in range(1, n + 1):
#         if visited[i] == False:
#             if isCycle(i, graph, visited, recursionPath):
#                 return "No"
#     return "Yes"
#
#
# # __Coding Ninjas Input Main___________________________________________
# t = int(input())
# while t > 0:
#     n, m = [int(i) for i in input().strip().split()]
#     prerequisites = [[int(i) for i in input().strip().split()] for j in range(m)]
#     res = canFinish(prerequisites, n, m)
#     print(res)
#     t = t - 1


# adjList[i[0]].append[i[1]]


def canFinish(numCourses, prerequisites):
    n = numCourses
    # 1. Construct a graph  from prerequisites::
    adjList = [[] for i in range(n)]
    for v1, v2 in prerequisites:
        adjList[v1].append(v2)
    print(adjList)

    # maintain visited array:
    visited = [0 for i in range(n)]

    # 2. DFS to check cycle::
    def dfs(i):
        if visited[i] == -1:
            return False

        if visited[i] == 1:
            return True

        visited[i] = -1
        for j in adjList[i]:
            print("j", j)
            if not dfs(j):
                return False

        visited[i] = 1
        return True

    # for all connected and disconnected graphs
    for i in range(numCourses):
        print('i', i)
        if not dfs(i):
            return False
    return True


numCourses = int(input())
# prerequisites = [[1, 0]]
# prerequisites = [[1, 2], [2, 3]]
prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(canFinish(numCourses, prerequisites))
