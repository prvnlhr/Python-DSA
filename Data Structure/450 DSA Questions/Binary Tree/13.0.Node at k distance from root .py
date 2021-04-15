import BinaryTreeInputPrint


def nodesAtDistanceK(root, k):
    if root is None:
        return None
    if k == 0:
        print(root.data)
    nodesAtDistanceK(root.left, k - 1)
    nodesAtDistanceK(root.right, k - 1)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
k = int(input())
ans = nodesAtDistanceK(root, k)
