from collections import defaultdict

# NOTE:: THIS IS A VARIATION OF "IS GRAPH BIPARTITE PROBLEM"
# ONLY THING THAT DIFFERS IN THIS PROBLEM, IS ITS STATEMENT AND INPUT TYPE
# IT USES CONCEPT OF "GRAPH COLORING"

'''
We want to split a group of n people (labeled from 1 to n) into two groups of any size. 
Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates 
that the person labeled ai does not like the person labeled bi, return true if it 
is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

 
'''


def possibleBipartition(n, dislikes):
    # 1. Make graph from given input size

    adjList = defaultdict(list)
    for connections in dislikes:
        a = connections[0]
        b = connections[1]
        adjList[a].append(b)
        adjList[b].append(a)

    colorArray = [-1 for i in range(n + 1)]

    def dfs(vertex):

        for adjNode in adjList[vertex]:

            if colorArray[adjNode] == -1:

                # 2. Give adjNode opposite color
                #  if vertex node is 1, adjNode would be 0
                colorArray[adjNode] = 1 - colorArray[vertex]
                if dfs(adjNode) == False:
                    return False
            else:
                if colorArray[adjNode] == colorArray[vertex]:
                    return False
        return True

    for i in range(len(colorArray)):
        if colorArray[i] == -1:
            ans = dfs(i)
            if ans == False:
                return False
    return True


testCases = [[[1, 2], [2, 3], [2, 4], [4, 5], [1, 5]], [[1, 3], [0, 2], [1, 3], [0, 2]],
             [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]]

for dislikes in testCases:
    ans = possibleBipartition(len(dislikes), dislikes)
    print(ans)
