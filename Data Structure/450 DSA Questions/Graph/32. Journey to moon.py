# ______________________________________________________________________________________________________________________
from collections import defaultdict


def journeyToMoon(n, astronaut):
    adjList = defaultdict(list)
    for a, b in astronaut:
        adjList[a].append(b)
        adjList[b].append(a)

    visited = [False for _ in range(n)]
    astroCount = [0]

    def dfs(vertex):
        if visited[vertex]:
            return

        visited[vertex] = True
        astroCount[0] += 1

        for j in adjList[vertex]:
            if not visited[j]:
                dfs(j)

    def countAstronauts():
        res = 0
        for i in range(n):
            if not visited[i]:
                astroCount[0] = 0
                dfs(i)
                x = n - astroCount[0]
                m = astroCount[0] * x
                res += m

        return res // 2

    return countAstronauts()


# ___________________________________________________________
def journeyToMoon2(n, astronaut):
    graph = defaultdict(list)
    for v1, v2 in astronaut:
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * n
    astroCount = [0]

    def dfs(node):
        astroCount[0] += 1
        visited[node] = True
        for adjNode in graph[node]:
            if visited[adjNode] == False:
                dfs(adjNode)

    res = 0
    eachC = []
    numCom = 0
    for vertex in range(n):
        if visited[vertex] == False:
            astroCount[0] = 0
            dfs(vertex)
            eachC.append(astroCount[0])
            numCom += 1
    totalWays = n * (n - 1) // 2
    sameWays = 0
    for i in range(numCom):
        sameWays += (eachC[i] * (eachC[i] - 1) // 2)
    return totalWays - sameWays

    # ___________________________________________________________________________________________________________


'''



    
    

'''

# ______________________________________________________________________________________________________________________
testCases = [[[4], [2],
              [[1, 2],
               [2, 3]]], [[5], [3],
                          [[0, 1],
                           [2, 3],
                           [0, 4]]], [[4], [2], [[1, 2], [2, 3]]], [[5], [3], [[0, 1], [2, 3], [0, 4]]],
             [[4], [1], [[0, 2]]],
             [[10], [20],
              [[0, 1],
               [0, 3],
               [0, 4],
               [2, 8],
               [1, 2],
               [1, 3],
               [1, 5],
               [1, 7],
               [1, 8],
               [1, 9],
               [2, 7],
               [3, 5],
               [3, 8],
               [6, 7],
               [3, 7],
               [4, 9],
               [4, 5],
               [4, 6],
               [4, 7],
               [6, 8]]]]
for test in testCases:
    V = test[0][0]
    astronaut = test[2]
    # print('test', V, astronaut)
    ans = journeyToMoon(V, astronaut)
    print('=', ans)
    print()

# 10 20
# 0 1
# 0 3
# 0 4
# 1 2
# 1 3
# 1 5
# 1 7
# 1 8
# 1 9
# 2 8
# 2 7
# 3 5
# 3 8
# 3 7
# 4 9
# 4 5
# 4 6
# 4 7
# 6 8
# 6 7
# __________
#
