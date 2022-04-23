from collections import defaultdict


# THIS IS BASED ON GRAPH COLOURING TECHNIQUE

def isGraphBipartite(graph):
    vertices = len(graph)
    colorArray = [-1] * vertices

    def dfs(node):

        for adjNode in graph[node]:

            if colorArray[adjNode] == -1:

                # color the adjNode node with opposite of node's color
                colorArray[adjNode] = 1 - colorArray[node]

                if not dfs(adjNode):
                    return False
            else:
                if colorArray[adjNode] == colorArray[node]:
                    return False
        return True

    for vertex in range(vertices):
        if colorArray[vertex] == -1:
            if dfs(vertex) == False:
                return False
    return True


testCases = [[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], [[1, 3], [0, 2], [1, 3], [0, 2]],
             [[2, 3, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 6, 9], [0, 1, 2, 3, 7, 8, 9], [0, 1, 2, 3, 4, 7, 8, 9], [0, 1, 2, 3, 5, 6, 8, 9],
              [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]]

for test in testCases:
    ans = isGraphBipartite(test)
    print(ans)
