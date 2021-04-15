import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    maxHeight = 1 + max(leftHeight, rightHeight)
    return maxHeight


def isBalanced(root):  # Time complexity is O(n*h) or O(n^2)
    if root is None:
        return 'true'
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1:
        return 'false'

    isLeftBalanced = isBalanced(root.right)
    isRightBalanced = isBalanced(root.left)

    if isLeftBalanced and isRightBalanced:
        return 'true'
    else:
        return 'false'


# Better Solution:
def isBalancedandHeight(root):
    if root is None:
        return 0, 'true'

    lh, isLeftBalanced = isBalancedandHeight(root.left)
    rh, isRightBalanced = isBalancedandHeight(root.right)

    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, 'false'

    else:
        return h, 'true'


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
x = int(input())
ans = height(root)
print(ans)
