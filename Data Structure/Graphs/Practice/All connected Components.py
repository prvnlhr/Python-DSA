## Read input as specified in the question.
## Print output as specified in the question.
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __dfsHelper(self, sv, visited, list):

        # print(sv, end = " ")
        list.append(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited, list)

        return list

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        final_list = []
        for i in range(self.nVertices):
            if not visited[i]:
                cc = self.__dfsHelper(i, visited, [])
                final_list.append(cc)

        # self.__dfsHelper(0, visited)
        return final_list


def allConnectedHelper(sv, visited, list):
    for i in range(g.nVertices):
        visited[sv] = True
        list.append(sv)
        if g.adjMatrix[sv][i] > 0 and visited[i] == False:
            allConnectedHelper(i, visited, list)
    return list


def allConnectedComp():
    visited = [False for i in range(g.nVertices)]
    ans = []
    for i in range(g.nVertices):
        if not visited[i]:
            list = allConnectedHelper(0, visited, [])
            ans.append(list)
    return ans


li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)

list = g.dfs()
for i in list:
    i.sort()
    for j in i:
        print(j, end=" ")
    print()
