import sys


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


Childsum = 0


def sumofNodes(tree):
    global Childsum
    for child in tree.children:
        Childsum = Childsum + child.data
    for child in tree.children:
        sumofNodes(child) + Childsum
    return Childsum + tree.data


# CN sol
def sumOfALLNodes(root):
    if root is None:
        return -sys.maxsize - 1
    total = 0

    for child in root.children:
        total = total + sumOfALLNodes(child)
    return total + root.data



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(sumOfALLNodes2(tree))
