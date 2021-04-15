import BinaryTreeInputPrint


def printLeafNodes(root):
    if root is None:
        return
    printLeafNodes(root.left)
    if root.left is None and root.right is None:
        print(root.data, end=' ')
    printLeafNodes(root.right)


def printLeftBoundary(root):
    if root is None:
        return
    if root.left is not None:
        print(root.data, end=' ')
        printLeftBoundary(root.left)
    elif root.right is not None:
        print(root.data, end=' ')
        printLeftBoundary(root.right)


def printRightBoundary(root):
    if root is None:
        return
    if root.right is not None:
        printRightBoundary(root.right)
        print(root.data, end=' ')
    elif root.left is not None:
        printRightBoundary(root.left)
        print(root.data, end=' ')


def printBoundary(root):
    if root is None:
        return
    print(root.data, end=' ')
    printLeftBoundary(root.left)
    printLeafNodes(root.left)
    printLeafNodes(root.right)
    printRightBoundary(root.right)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = printBoundary(root)
print(ans)
