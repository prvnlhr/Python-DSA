# POINTS TO REMEMBER:
# Inorder traversal of BST gives sorted array.
import BST


def constructBST(sortedArr):
    if len(sortedArr) <= 0:
        return None
    middle_distance = len(sortedArr) // 2
    middle_element = sortedArr[middle_distance]
    root = BST.BinaryTreeNode(middle_element)

    root.left = constructBST(sortedArr[:middle_distance])
    root.right = constructBST(sortedArr[middle_distance + 1:])
    return root


def getInorder(root, arr):
    if root is None:
        return None

    getInorder(root.left, arr)
    arr.append(root.data)
    getInorder(root.right, arr)


def sortedArrayToBST(arr, root):
    if root is None:
        return
    # first update the left subtree
    sortedArrayToBST(arr, root.left)
    root.data = arr[0]
    arr.pop()
    sortedArrayToBST(arr, root.right)


def binaryTreeToBST(root):
    if root is None:
        return
    # STEP__1. getInorder of BT
    inorder = []
    getInorder(root, inorder)
    # STEP__2. sort the inorder of BT
    inorder.sort()
    # STEP__3. update BT using sorted inorder
    # NOTE:: we are not making new BST from sorted inorder, we are just updating the BT elements
    sortedArrayToBST(inorder, root)


btRoot = BST.buildLevelTree()
root = binaryTreeToBST(btRoot)
BST.PrintLevelWise(root)
