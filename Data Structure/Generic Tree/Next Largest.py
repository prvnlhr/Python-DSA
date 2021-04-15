class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

import queue

def nextLargest(tree, n):
    dict = []
    resarray = helper(tree , n , dict)
    l = len(resarray)
    min = 2653165598
    Node = None
    # print(type(min))
    for i in range(l):
        if resarray[i].data < min:
            min = resarray[i].data
            Node = resarray[i]
        # print(resarray[i] , resarray[i].data)
    return (Node)





def helper(tree , n , dict):

    if tree == None:
        return
    if tree.data > n:
        dict.append(tree)


    for child in tree.children:
        helper(child , n , dict)

    return dict












def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)
