import queue
import sys


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def numNodes(root):
    if root is None:
        return 0
    return 1 + numNodes(root.left) + numNodes(root.right)


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree 
    if key < root.data:
        root.left = deleteNode(root.left, key)

    # If the key to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif (key > root.data):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root


# def removeNode(root, x):
#     if root is None:
#         return root
#     if root.data == x:
#         if root.right != None:
#             root == root.right
#         elif root.left != None:
#             root == root.left.data
#         else:
#             root.data == None
#
#     removeNode(root.left, x)
#     removeNode(root.right, x)
#
def min(root):
    if root == None:
        return 10000

    if root.left == None:
        return root.data
    return min(root.left)


def deleteDataHelper(root, data):
    if root == None:
        return False, None

    if root.data < data:
        deleted, newRightNode = deleteDataHelper(root.right, data)
        root.right = newRightNode
        return deleted, root

    if root.data < data:
        deleted, newleftNode = deleteDataHelper(root.left, data)
        root.left = newleftNode
        return deleted, root

    if root.left == None and root.right == None:
        return True, None

    if root.left == None:
        return True, root.right
    if root.right == None:
        return True, root.left

    replacement = min(root.right)
    root.data = replacement
    deleted, newRightNode = deleteDataHelper(root.right, replacement)
    root.right = newRightNode
    return True, root


def delete(root, data):
    deleted, newRoot = deleteDataHelper(root, data)
    if deleted:
        root = newRoot
        return deleted


def printLevelATNewLine(root):
    if root == None:
        return
    inputInQueue = queue.Queue()
    outputfromQueue = queue.Queue()
    inputInQueue.put(root)
    while not inputInQueue.empty():
        while not inputInQueue.empty():
            curr = inputInQueue.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputfromQueue.put(curr.left)
            if curr.right != None:
                outputfromQueue.put(curr.right)
        print()
        inputInQueue, outputfromQueue = outputfromQueue, inputInQueue


# _________________________________________________________________________________________

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
x = int(input())
deleteNode(root, x)
printLevelATNewLine(root)
