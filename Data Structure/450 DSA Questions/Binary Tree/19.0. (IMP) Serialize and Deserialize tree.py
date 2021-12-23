import queue

import BinaryTreeInputPrint

res = []


def deserializeHelper(arr):
    print(arr)
    if arr[0] == 'x':
        return None
    newNode = BT.BinaryTreeNode(arr[0])
    newNode.left = deserializeHelper(arr[1:])
    newNode.right = deserializeHelper(arr[1:])
    return newNode


def deserialize(serializeStr):
    arr = serializeStr.split(',')
    print(arr)
    newRoot = deserializeHelper(arr)
    BT.PrintLevelWise(newRoot)


def serialize(root):
    if root is None:
        return 'x'
    leftStr = serialize(root.left)
    rightStr = serialize(root.right)
    return str(root.data) + ',' + leftStr + ',' + rightStr


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
serializeStr = serialize(root)
print(serializeStr)
deserialize(serializeStr)
