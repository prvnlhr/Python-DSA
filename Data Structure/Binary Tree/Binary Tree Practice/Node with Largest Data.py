import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# my sol
largest = -54454
largestNode = None
def LargestNode(root):
    if root is None:
        return
    global largest
    global largestNode
    if root.data > largest:
        largestNode = root
        largest = root.data
    LargestNode(root.left)
    LargestNode(root.right)
    return largestNode

# CN sol
def Largest(root):
    if root == None:
        return -1
    leftlargest = Largest(root.left)
    rightLargest  = Largest(root.right)
    largest = max(leftlargest , rightLargest ,root.data)
    return largest

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
ansNode = LargestNode(root)
print(ansNode.data)
