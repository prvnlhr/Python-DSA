import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeafNodes(root):
    if root is None:
        return
    printLeafNodes(root.left)
    if root.left is None and root.right is None:
        print(root.data, end=' ')
    printLeafNodes(root.right)


def printLeftBoundary(root):
    if root is None:
        return
    if root.left is not None:
        print(root.data, end=' ')
        printLeftBoundary(root.left)
    elif root.right is not None:
        print(root.data, end=' ')
        printLeftBoundary(root.right)


def printRightBoundary(root):
    if root is None:
        return
    if root.right is not None:
        printRightBoundary(root.right)
        print(root.data, end=' ')
    elif root.left is not None:
        printRightBoundary(root.left)
        print(root.data, end=' ')


def printBoundary(root):
    if root is None:
        return
    print(root.data, end=' ')
    printLeftBoundary(root.left)
    printLeafNodes(root.left)
    printLeafNodes(root.right)
    printRightBoundary(root.right)


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


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printBoundary(root)
