import BinaryTreeInputPrint


def findPath(root, pathArr, node):
    if root is None:
        return False

    pathArr.append(root.data)
    if root.data == node:
        return True
    if findPath(root.left, pathArr, node) or findPath(root.right, pathArr, node):
        return True
    pathArr.pop()
    return False


def pathToNode(root, node):
    pathArray = []
    if (findPath(root, pathArray, node)):
        print(pathArray)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
node = int(input())
# n2 = int(input())
pathToNode(root, node)
