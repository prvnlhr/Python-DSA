import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
