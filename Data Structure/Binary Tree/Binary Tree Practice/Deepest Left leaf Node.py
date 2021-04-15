import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# mysol correct :
def helper(root, isLeft):
    global maxLeaf
    if root is None:
        return None
    if isLeft is True:

        if root.left is None and root.right is None:
            if root.data > helper.maxLeaf:
                helper.maxLeaf = root.data
    helper(root.left, True)
    helper(root.right, False)

def deepestLeftNode(root):
    helper.maxLeaf = -65523
    helper(root, False)
    return helper.maxLeaf

# GeeksForGeeks
def deepestLeftLeafUtil(root, lvl, maxlvl, isLeft):
    # Base Case
    if root is None:
        return

    # Update result if this node is left leaf and its
    # level is more than the max level of the current result
    if (isLeft is True):
        if (root.left == None and root.right == None):
            if lvl > maxlvl[0]:
                deepestLeftLeafUtil.resPtr = root
                maxlvl[0] = lvl
                return

    # Recur for left and right subtrees
    deepestLeftLeafUtil(root.left, lvl + 1, maxlvl, True)
    deepestLeftLeafUtil(root.right, lvl + 1, maxlvl, False)


# A wrapper for left and right subtree
def deepestLeftLeaf(root):
    maxlvl = [0]
    deepestLeftLeafUtil.resPtr = None
    deepestLeftLeafUtil(root, 0, maxlvl, False)
    return deepestLeftLeafUtil.resPtr


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
ans = deepestLeftNode(root)
print(ans)
