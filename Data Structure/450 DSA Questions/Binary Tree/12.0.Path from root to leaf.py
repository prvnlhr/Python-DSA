import BinaryTreeInputPrint


def Helper(root, path):
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None:
        print(path)
    Helper(root.left, path)
    Helper(root.right, path)
    path.pop()


def rootToLeafPath(root):
    path = []
    Helper(root, path)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = rootToLeafPath(root)
