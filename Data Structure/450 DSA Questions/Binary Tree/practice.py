import BinaryTreeInputPrint


# 2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1

def Helper(root, x, path):
    if root is None:
        return
    if root.left is None and root.right is None and x == root.data:
        print(*path)
    path.append(root.data)
    Helper(root.left, x - root.data, path)
    Helper(root.right, x - root.data, path)
    path.pop()

    # if root == None:
    #     return
    # if root.left == None and root.right == None:
    #     if root.data == k:
    #         print(*lst, k)
    #     return
    # lst.append(root.data)
    # rootToLeafPathsSumToK(root.left, k - root.data, lst)
    # rootToLeafPathsSumToK(root.right, k - root.data, lst)
    # lst.pop()


def rootToLeafPathsSumToK(root, k, lst):
    if root == None:
        return
    if root.left == None and root.right == None:
        if root.data == k:
            print(*lst, k)
        return
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k - root.data, lst)
    rootToLeafPathsSumToK(root.right, k - root.data, lst)
    lst.pop()


def runnerFunction(root):
    path = []
    x = 23
    return Helper(root, x, path)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = runnerFunction(root)
print(ans)
# BT.PrintLevelWise(ans)
