import queue


# Time Complexity__
# If the graph is represented as adjacency list:: O(V) + O(E) = O(V + E)
# If the graph is represented as an adjacency matrix (a V x V array):  O(V * V) = O(V2).

# Space Complexity__
# Since we are maintaining a priority queue (FIFO architecture)
# to keep track of the visited nodes, in worst case,
# the queue could take up to the size of the nodes(or vertices) in the graph.
# Hence, the space complexity is O(V).
class Graph:

    def __init__(self, nVertics):
        self.nVertices = nVertics
        self.adjMatrix = [[0 for i in range(nVertics)] for j in range(nVertics)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def bfs_helper(self, visited, nVertices, sv):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            vertex = q.get()
            print(vertex, end='')
            for i in range(nVertices):
                if (self.adjMatrix[vertex][i] > 0 and visited[i] == False):
                    q.put(i)
                    visited[i] = True

    def Bfs(self, V):
        visited = [False for i in range(self.nVertices)]
        ans = self.bfs_helper(visited, V, 0)


edgeVertices = [int(i) for i in input().strip().split()]
V = int(edgeVertices[0])
E = int(edgeVertices[1])
g = Graph(V)

for i in range(E):
    arr = [int(i) for i in input().strip().split()]
    v1 = int(arr[0])
    v2 = int(arr[1])
    g.addEdge(v1, v2)

g.Bfs(V)
