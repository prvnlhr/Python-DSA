import BinaryTreeInputPrint


def pathSumHelper(root, sum, path, result):
    if root is None:
        return None

    if root.data == sum and root.left is None and root.right is None:
        result.append([*path, root.data])
        print(result)
        return None
    path.append(root.data)
    pathSumHelper(root.left, sum - root.data, path, result)
    pathSumHelper(root.right, sum - root.data, path, result)
    path.pop()


def pathSum(root, sum):
    result = []
    pathSumHelper(root, sum, [], result)
    return result


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
sum = int(input())
ans = pathSum(root, sum)
print(ans)
# BT.PrintLevelWise(root)
