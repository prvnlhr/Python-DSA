import sys


# Bellman-Ford does not work with undirected graph with negative
def bellman_ford(edgeList, V, src):
    # maintaining distArray which will give shortest distance from src of all nodes
    distArray = [sys.maxsize for _ in range(V)]
    # initialize distArray at src vertex = 0
    distArray[src] = 0

    # now for no_of_edges - 1 time do relaxation step for every edge in edge list
    for i in range(V - 1):
        for edge in edgeList:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            # relaxation step:
            if distArray[u] + w < distArray[v]:
                # update the distance array
                distArray[v] = distArray[u] + w
    # Now , if we do one more final relaxation step and if distance is
    # still reducing,then we have a negative cycle.

    isNegativeCyle = False
    for edge in edgeList:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        # distance is still decreasing,if condition will run and distArray will have negative edges again.
        if distArray[u] + w < distArray[v]:
            distArray[v] = distArray[u] + w
            # if distance decreased,negative cycle and no need to run loop further
            isNegativeCyle = True
            print('Negative cycle detected')
            break

    # if negative cycle detect, isNegative would be True,
    if isNegativeCyle == False:
        print(distArray)


# Ex. 1__
# 6 7
# 3 2 6
# 5 3 1
# 0 1 5
# 1 5 -3
# 1 2 -2
# 3 4 -2
# 2 4 3
#
# Ex. 2__
# 5 8
# 0 1 -1
# 0 2 4
# 1 2 3
# 1 3 2
# 1 4 2
# 3 2 5
# 3 1 1
# 4 3 -3

V, E = [int(i) for i in input().strip().split()]

# NOTE :: We need and edge array because it is simple to iterate in bellman ford, since we just need all edges
edgeList = []
print(edgeList)

for i in range(E):
    arr = [int(j) for j in input().strip().split()]
    node1 = int(arr[0])
    node2 = int(arr[1])
    weight = int(arr[2])
    pair = [node1, node2, weight]
    edgeList.append(pair)
src = int(input('Enter source vertex :'))
for node in edgeList:
    print(node)
bellman_ford(edgeList, V, src)
