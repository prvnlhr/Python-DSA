import queue

import BinaryTreeInputPrint


def leftViewHelper2(root):
    if root is None:
        return
    q = []
    q.append(root)
    result = []
    while len(q):
        n = len(q)
        for i in range(1, n + 1):
            ele = q[0]
            q.pop()
            if i == 1:
                result.append(ele.data)
            if ele.left is not None:
                q.append(ele.left)
            if ele.right is not None:
                q.append(ele.right)
    print(result)


# _ O(N)
result = []


def leftViewHelper(root, level, max_level):
    global result
    if root is None:
        return
    if max_level[0] < level:
        result.append(root.data)
        print(root.data, end=' ')
        print(max_level)
        max_level[0] = level
    leftViewHelper(root.left, level + 1, max_level)
    leftViewHelper(root.right, level + 1, max_level)


def leftView(root):
    level = 1
    max_level = [0]
    leftViewHelper(root, level, max_level)
    return result
    # return leftViewHelper2(root)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = leftView(root)
print(result)
# 2 2 13 7 10 1 10 5 2 -1 14 5 11 5 5 13 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
