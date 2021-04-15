from Edge import Edgelist


def kruskalAlgo(edgeList, V):
    edgeList = sorted(edgeList, key=lambda e: e.w)
    parentArray = [i for i in range(V)]
    mst = []
    count = 0
    i = 0
    while count < (V - 1):
        currentEdge = edgeList[i]
        v1parent = findParent(parentArray, currentEdge.v1)
        v2parent = findParent(parentArray, currentEdge.v2)
        if v1parent != v2parent:
            mst.append(currentEdge)
            count = count + 1
            parentArray[v1parent] = v2parent
        i = i + 1
    return mst


def findParent(parentArray, v):
    if parentArray[v] == v:
        return v
    return findParent(parentArray, parentArray[v])


# Main__
VerticeEdge = input().strip().split()
V = int(VerticeEdge[0])
E = int(VerticeEdge[1])
edgeList = []
for i in range(E):
    V1V2W = input().strip().split()
    v1 = int(V1V2W[0])
    v2 = int(V1V2W[1])
    w = int(V1V2W[2])
    e = Edgelist(v1, v2, w)
    edgeList.append(e)

# for i in edgeList:
#     print(i.v1, i.v2, i.w)
mst = kruskalAlgo(edgeList, V)

for i in mst:
    print(i.v1, i.v2, i.w)
