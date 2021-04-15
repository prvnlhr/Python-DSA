import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


count = 0


def countNodesGreaterThanX(root, x):
    global count

    if root == None:
        return 0
    if root.data > x:
        count = count + 1
    leftlargest = countNodesGreaterThanX(root.left, x)
    rightLargest = countNodesGreaterThanX(root.right, x)

    return count


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
x = int(input())
root = buildLevelTree(levelOrder)
print(countNodesGreaterThanX(root, x))
