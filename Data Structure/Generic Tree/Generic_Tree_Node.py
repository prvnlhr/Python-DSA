#_______________________________________________________________________________________________________________________
class GenericTreeNode:
    def __init__(self , data):
        self.data = data
        self.children = list()
#_______________________________________________________________________________________________________________________

def printTree(root):
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,":",end=" ")
    for child in root.children:
        print(child.data,",",end=" ")
    print()
    for child in root.children:
        printTreeDetailed(child)


def takeTreeInput():

    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    root = GenericTreeNode(rootData)
    print("Enter Number of children of", rootData)
    childrencount = int(input())
    for i in range(childrencount):
        child = takeTreeInput()
        root.children.append(child)
    return root

def NumNodes(root):
    count = 1
    for child in root.children:
        count = count + NumNodes(child)
    return count

Childsum = 0
def SumofAllNodes(root):
    global Childsum
    for child in root.children:
        Childsum = Childsum + child.data

    for child in root.children:
        SumofAllNodes(child) + Childsum

    return Childsum + root.data
largest = -11651
def maxDataNode(root):
    global largest
    if root == None:
        return None


    for child in root.children:
        if child.data > largest:
            largest = child.data


    for child in root.children:
        maxDataNode(child)

    return  largest

def maxDataNode(tree):
    if tree == None:
        return
    max = tree

    for child in tree.children:
        if max.data < maxDataNode(child).data:
            max = maxDataNode(child)

    return max

def height(tree):
    ans = 0
    for child in tree.children:
        childheight = height(child)
        if childheight > ans:
            ans = childheight
    return ans + 1


def containsX(tree,x):
    if tree == None:
        return False
    if tree.data == x:
        return True
    for child in tree.children:
        if containsX(child , x):
            return True
    return False















# Main Driver___________________________________________________________________________________________________________
# n1 = GenericTreeNode(5)
# n2 = GenericTreeNode(2)
# n3 = GenericTreeNode(9)
# n4 = GenericTreeNode(8)
# n5 = GenericTreeNode(7)
# n6 = GenericTreeNode(15)
# n7 = GenericTreeNode(1)
#
# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)
#
# n3.children.append(n6)
# n3.children.append(n7)
# x = int(input())

# root = takeTreeInput()
# printTree(root)
# print()
# printTreeDetailed(root)
# ans = print("ans",NumNodes(root))
# res = SumofAllNodes(root)
# print(res)
# largestvalue = maxDataNode(root)
# print(largestvalue)
# h = height(root)
# print(h)
# if containsX(root,x):
#     print('true')
# else:
#     print('false')
