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


def nodesAtDistanceK(root, node, k):
    printkdistanceNode(root, node, k)


def printkdistanceNodeDown(root, k):
    if root == None or k < 0:
        return
    if k == 0:
        print(root.data, end="")
        print()
        return

    printkdistanceNodeDown(root.left, k - 1)
    printkdistanceNodeDown(root.right, k - 1)


def printkdistanceNode(root, target, k):
    if root == None:
        return -1
    if root.data == target:
        printkdistanceNodeDown(root, k)
        return 0
    dl = printkdistanceNode(root.left, target, k)
    if dl != -1:
        if dl + 1 == k:
            print(root.data, end="")
            print()
        else:
            printkdistanceNodeDown(root.right, k - dl - 2)
            return 1 + dl
    dr = printkdistanceNode(root.right, target, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data, end="")
            print()
        else:
            printkdistanceNodeDown(root.left, k - dr - 2)
            return 1 + dr
    return -1


levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

node = int(input())
k = int(input())
nodesAtDistanceK(root, node, k)
