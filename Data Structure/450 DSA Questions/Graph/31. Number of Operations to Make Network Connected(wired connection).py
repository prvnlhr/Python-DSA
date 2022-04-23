# There are n computers numbered from 0 to n - 1 connected by ethernet
# cables connections forming a network where connections[i] = [ai, bi]
# represents a connection between computers ai and bi. Any computer can
# reach any other computer directly or indirectly through the network.
#
# You are given an initial computer network connections. You can extract
# certain cables between two directly connected computers, and place
# them between any pair of disconnected computers to make them directly
# connected.
#
# Return the minimum number of times you need to do this in order to
# make all the computers connected. If it is not possible, return -1.


# CONCEPT:__________________________________________________________________
# IN A GRAPH , minimum no of edges to connect all vertices
# is given as ,
# NO. of MINIMUM REQUIRED EDGES = NO. of VERTICES - 1

# Now, according to problem statement, we want to make connections, between all
# computers, and number of edges required should be enough to connect them all.
# Now, we consider all computers as components,so we need to connect all
# components with minimum edges.
# So our problem it two find how many min edges we will required to connect all components.
# now, in problem we are given no of vertices(n) and connections = [,,,,,],
# which defines edges between vertices. if there is edge there are directly connected.

# Now there are two conditions, to look forward, i.e, if we have V vertices ,then
# 1. How many min edges are required to connect the all ??, So the ans is,
# NO. of MINIMUM REQUIRED EDGES = NO. of VERTICES - 1,
# if this connection does not satisfies means we don't have enough edges ,
# to make new connections.
# now if first conditions is full filled, then the, problem is half solved.
# So now we have enough edges, then we need to calculate minimum connections to
# make to connect all components as we are considering computers as component.
# So how to find minimum connections..??
# if we look carefully , then find the minimum connections, to
# connect all components is == No. of components - 1
# So the problem boils down to finding no of components,
# which is as simply and plain DFS traversal and increasing the count,
# and at end returning count-1


from collections import defaultdict


def makeConnected(n, connections):
    adjList = defaultdict(list)

    # 1. making graph ,adjList
    for a, b in connections:
        adjList[a].append(b)
        adjList[b].append(a)

    visited = [False for _ in range(n)]
    num_vertices = n
    num_edges = len(connections)

    # Condition 1: if we have enough edges to make connections, i.e extra edges
    if num_edges < num_vertices - 1:
        return -1

    def dfs(vertex):
        visited[vertex] = True

        for adjNode in adjList[vertex]:
            if not visited[adjNode]:
                dfs(adjNode)

    # Find the no of components
    def noOfComponents():
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        # return no_of_components - 1
        return count - 1

    return noOfComponents()


testCases = [[[4], [[0, 1], [0, 2], [1, 2]]], [[6], [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]],
             [[6], [[0, 1], [0, 2], [0, 3], [1, 2]]]]

for test in testCases:
    n = test[0][0]
    connections = test[1]
    ans = makeConnected(n, connections)
    print(ans)
