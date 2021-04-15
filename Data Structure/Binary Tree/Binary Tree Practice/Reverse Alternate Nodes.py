import queue
from queue import Queue


# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ________________________________________________________________________________________________________________________
def reverseAlternate(root):
    reverseAlternateHelper(root.left, root.right, 0)


def reverseAlternateHelper(root1, root2, level):
    if root1 is None or root2 is None:
        return
    if level % 2 == 0:
        temp = root1.data
        root1.data = root2.data
        root2.data = temp

    reverseAlternateHelper(root1.left, root2.right, level + 1)
    reverseAlternateHelper(root1.right, root2.left, level + 1)


# ______________________________________________________________________________________________________________________
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


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


# Driver Function:
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
# PrintLevelWise(root)
reverseAlternate(root)
inOrder(root)
