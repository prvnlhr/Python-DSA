from Implement_Graph import Graph

def dfs(sv, visited):
    visited[sv] = True
    for i in range(g.nVertices):
        if g.adjMatrix[sv][i] > 0 and visited[i] == False:
            dfs(i, visited)
            visited[i] = True




#__There are two dfs functions 1 and 2:
# function 1 only applicable for connected graph
# function 2 is applicable for both connected and non connected because we are checking remaining vertices from visited
# array that is any vertex in visited is still false that means we still need to explore
#__1.
def isConnected():
    visited = [False for i in range(g.nVertices)]
    dfs(0, visited)
    for val in visited:
        if not val:
            return False
    return True

# __Main________________________________________________________________________________________________________________
li = input().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)
for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)

print()
if isConnected():
    print('true')
else:
    print('false')

