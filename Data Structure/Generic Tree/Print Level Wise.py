class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

#____My solution 100% correct___________________________________________________________________________________________________________________
def printLevelWiseTree(tree):
    q = [tree]
    newq = []
    level = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=':')

        for child in parent.children:
            newq.append(child)
            level.append(child)

        l = len(level)
        if l != 0:
            for i in range(l):
                if i == l - 1:
                    print(level[i].data, end="")

                else:
                    print(level[i].data, end=",")
        level = []
        print()

        if len(q) == 0:
            q = newq
            newq = []
#_______________________________________________________________________________________________________________________
def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line


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
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
print()
printLevelAtNewLine(tree)
