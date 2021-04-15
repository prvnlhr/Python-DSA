import BinaryTreeInputPrint


def pathSum(root, sum):
    if root is None:
        return False
    if root.data == sum and root.left is None and root.right is None:
        return True
    else:
        return pathSum(root.left, sum - root.data) or pathSum(root.right, sum - root.data)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
sum = int(input())
ans = pathSum(root, sum)
print(ans)
# BT.PrintLevelWise(root)
