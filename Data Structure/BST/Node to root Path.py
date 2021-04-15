import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodeToRootPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l
    leftOutput = nodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput = nodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
lst = [int(i) for i in input().strip().split()]
root = constructBST(lst)
preOrder(root)
