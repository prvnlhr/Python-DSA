import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


ans = -1

# CodeZen Passes 4/6 test cases:
def postorderSuccessor(root, x):
    global ans

    if root is None:
        return -1

    if root.right != None and root.right.data == x:
        ans = root.data

    if root.left != None and root.left.data == x:
        if root.right != None:
            ans = root.right.data
        else:
            ans = -1

    postorderSuccessor(root.left, x)
    postorderSuccessor(root.right, x)
    return ans


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

        print(currData, ":L:", left, " R:", right, sep='')


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


# Driver Function:
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
x = int(input())
ans = postorderSuccessor(root, x)
PrintLevelWise(root)
print(ans)
