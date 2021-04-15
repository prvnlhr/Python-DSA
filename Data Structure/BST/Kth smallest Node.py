import queue
import sys


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# _GEEKS fOR GEEKS_______________________________________________________________________
max = sys.maxsize
min = -sys.maxsize - 1

def kthSmallest(root, k):
    # Base case
    if (root == None):
        return None
    if root.left is None and root.right is None:
        return root

    # Search in left subtree
    left = kthSmallest(root.left, k)

    # If k'th smallest is found in
    # left subtree, return it
    if (left != None):
        return left

    # If current element is k'th
    # smallest, return it
    k -= 1
    if (k == 1):
        return root

    # Else search in right subtree
    return kthSmallest(root.right, k)


# Function to find k'th largest element in BST
def printKthSmallest(root, k):
    # Maintain index to count number
    # of nodes processed so far
    count = 0
    res = kthSmallest(root, k)

    if (res == None):
        print(min)
    else:
        print(res.data)


# __CN SOL_______________________________________
def numNodes(root):
    if root is None:
        return 0
    return 1 + numNodes(root.left) + numNodes(root.right)


def findNode(root, k):
    if root is None:
        return -sys.maxint - 1
    leftcount = numNodes(root.left)
    if leftcount >= k:
        return findNode(root.left)
    elif leftcount == k - 1:
        return root.data
    else:
        return findNode(root.right, k - leftcount - 1)


# __________________________________________________________________________________________

# My sol:_Passes all cases correct sol:
def kthSmallestNode(root, k):
    output = []
    kthSmallestNodeHelper(root, k, output)
    if len(output) == 0:
        return -sys.maxint - 1

    for i in range(len(output)):
        if i == k - 1:
            return output[i]


def kthSmallestNodeHelper(root, k, output):
    if root is None:
        return None
    kthSmallestNodeHelper(root.left, k, output)
    output.append(root.data)
    kthSmallestNodeHelper(root.right, k, output)
# ____________________________________________________________________________________________

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
k = int(input())
ans = kthSmallestNode(root, k)
print(ans)
