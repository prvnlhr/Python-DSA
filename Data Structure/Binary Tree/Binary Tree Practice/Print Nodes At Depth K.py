import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# v1_________________________________________________
def printDepthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k - 1)
    printDepthK(root.right, k - 1)


# v2__________________________________________________
def printDepthKv2(root, k, d=0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    printDepthKv2(root.left, k, d + 1)
    printDepthKv2(root.right, k, d + 1)


# _________________________________________________
def PrintLevelWise(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)

    while (not q.empty()):
        curr = q.get()
        currData = curr.data
        left = -1
        right = -1
        if curr.left != None:
            left = curr.left.data
            q.put(curr.left)
        if curr.right != None:
            right = curr.right.data
            q.put(curr.right)

        print(currData, ":L:", left, "R:", right, sep='')


def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter root ")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not (q.empty())):
        currentnode = q.get()
        print("Enter Left Child of ", currentnode.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            currentnode.left = leftChild
            q.put(leftChild)

        print("Enter right Child of ", currentnode.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currentnode.right = rightChild
            q.put(rightChild)

    return root


# Driver Function:
root = takeLevelWiseTreeInput()
k = int(input())
# v1____________________
printDepthK(root, k)
# v2____________________
printDepthKv2(root, k)
