import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


# Problem ID 353, Level order traversal
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root == None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ


# ______________________________________________________________________________________________________________________
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def isBalanced(root):  # Time Complexity O(n*h) or O(n^2)
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBlanaced = isBalanced(root.right)
    if isLeftBalanced and isRightBlanaced:
        return True
    else:
        return False


# Better Solution:
def getHeightandCheckBalanced(root):  # Time Complexity : O(n)
    if root == None:
        return 0, True
    lh, isLeftBalanced = getHeightandCheckBalanced(root.left)
    rh, isRightBalanced = getHeightandCheckBalanced(root.right)

    h = 1 + max(lh, rh)

    if lh - rh > 1 or rh - lh > 1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False


# _______________________________________________________________________________________________________________________
# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(getHeightandCheckBalanced(root))
