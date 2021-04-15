import BinaryTreeInputPrint


def mirrorTree(root):
    if root is None:
        return

    mirrorTree(root.left)
    mirrorTree(root.right)
    if root.left and root.right:
        root.left.data, root.right.data = root.right.data, root.left.data


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
mirrorTree(root)
BT.PrintLevelWise(root)
