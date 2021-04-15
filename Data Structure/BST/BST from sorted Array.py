import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    l = len(lst)
    if lst == None or l <= 0:
        return None
    mid = (l - 1) // 2
    rootData = lst[mid]
    newNode = BinaryTreeNode(rootData)
    root.left = constructBST(lst[:mid])
    root.right = constructBST(lst[mid + 1:])
    return root


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
