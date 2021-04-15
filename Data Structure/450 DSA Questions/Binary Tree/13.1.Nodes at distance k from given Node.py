import BinaryTreeInputPrint


def nodesAtDistanceK(root, k, dist, result):
    if root is None:
        return

    elif k == 0:
        print(root.data)
        result.append(root.data)

    nodesAtDistanceK(root.left, k, dist + 1, result)
    nodesAtDistanceK(root.right, k, dist + 1, result)


def nodesAtDistanceKFromGivenNode(root, k, node, result):
    if root is None:
        return -1

    elif root.data == node:
        nodesAtDistanceK(root, k, 0, result)
        return 1
    else:
        L = nodesAtDistanceKFromGivenNode(root.left, k, node, result)
        R = nodesAtDistanceKFromGivenNode(root.right, k, node, result)
        if L != -1:
            if L == k:
                print(root.data)
                result.append(root.data)
            nodesAtDistanceK(root.right, k, L + 1, result)
            return L + 1
        elif R != -1:
            if R == k:
                print(root.data)
                result.append(root.data)
            nodesAtDistanceK(root.left, k, R + 1, result)
            return R + 1
        else:
            return -1
    # return result


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
k = int(input())
node = int(input())
# result array to store all nodes
result = []
ans = nodesAtDistanceKFromGivenNode(root, k, node, result)
print(ans)
