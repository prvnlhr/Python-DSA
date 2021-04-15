import BinaryTreeInputPrint


# __O(n^2):
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)


def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False

    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)

    if isRightBalanced and isLeftBalanced:
        return True


# O(n):
def isBalancedAndHeight(root):
    if root is None:
        return 0, True

    lh, isLeftBalanced = isBalancedAndHeight(root.left)
    rh, isRightBalanced = isBalancedAndHeight(root.right)
    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    else:
        return h, True


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = isBalanced(root)
print(ans)
# BT.PrintLevelWise(root)
