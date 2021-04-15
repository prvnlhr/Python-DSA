from Edge import Edgelist


def kruskal(edgelist, V):
    # ___step 1 : sorting edgelist on basis of its weight
    edgelist = sorted(edgelist, key=lambda e: e.w)

    # ___step 2 : creating parent array and initializing with default values same as index for storing every vertex's parent
    parentarray = [i for i in range(V)]

    # ___step 3 : creating mst to store output final edges
    mst = []

    count = 0
    i = 0
    while count < (V - 1):
        currentEdge = edgelist[i]
        v1parent = getParent(currentEdge.v1, parentarray)
        v2parent = getParent(currentEdge.v2, parentarray)
        if v1parent != v2parent:
            mst.append(currentEdge)
            count = count + 1
            parentarray[v1parent] = v2parent
        i = i + 1
    return mst


def getParent(v, parentarray):
    if parentarray[v] == v:
        return v
    return getParent(parentarray[v], parentarray)


# __Main Function________________________________________________________________________________________________________
li = input().strip().split()
V = int(li[0])
E = int(li[1])
edgelist = []

for i in range(E):
    arr = input().strip().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    weight = int(arr[2])
    e = Edgelist(v1, v2, weight)
    edgelist.append(e)
mst = kruskal(edgelist, V)
for i in mst:
    if i.v2 > i.v1:
        print(str(i.v1) + " " + str(i.v2) + " " + str(i.w))
    else:
        print(str(i.v2) + " " + str(i.v1) + " " + str(i.w))
