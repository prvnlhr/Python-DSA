# An undirected graph is tree if it has following properties.
# 1) There is no cycle.
# 2) The graph is connected.
from collections import defaultdict


class Solution:

    def detectCycle(self, adjList, visited, sv, parent):

        visited[sv] = True

        for j in adjList[sv]:

            if visited[j] == False:
                if self.detectCycle(adjList, visited, j, sv) == True:
                    return True
            elif j != parent:
                return True
        return False

    def isConnected(self, visited, V):
        for i in range(V):
            if visited[i] == False:
                return False

    def checkIfTree(self, adjList, V):
        visited = [False for i in range(V)]

        isCycle = self.detectCycle(adjList, visited, 0, -1)
        print('isCycle', isCycle)
        if isCycle:
            return False
        isConnected = self.isConnected(visited, V)
        print('isConnected', isConnected)
        if isConnected == False:
            return False
        else:
            return True


V, E = [int(i) for i in input().strip().split()]
# adjList = [[] for i in range(V)]
adjList = defaultdict(list)
for i in range(E):
    edges = [int(i) for i in input().strip().split()]
    a = int(edges[0])
    b = int(edges[1])
    print(a, b)
    adjList[a].append(b)
    adjList[b].append(a)
x = 0
print(adjList)
ob = Solution()
ans = ob.checkIfTree(adjList, V)
print(ans)
