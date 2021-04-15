import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# _________________________________________________
# CN sol
def isNodePresent(root, x):
    if root is None:
        return 'false'
    if root.data == x:
        return 'true'
    return (isNodePresent(root.left, x) or isNodePresent(root.right, x))


# My Sol
isPresent = False


def isNodePresent(root, x):
    global isPresent
    if root == None:
        return False
    if root.data == x:
        isPresent = True
        return isPresent
    isNodePresent(root.left, x)
    isNodePresent(root.right, x)
    return isPresent


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
x = int(input())
ans = isNodePresent(root, x)
print(ans)
