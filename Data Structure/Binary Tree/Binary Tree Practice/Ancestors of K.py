import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# mysol correct :
def helper(root, isLeft):
    global maxLeaf
    if root is None:
        return None
    if isLeft is True:

        if root.left is None and root.right is None:
            if root.data > helper.maxLeaf:
                helper.maxLeaf = root.data
    helper(root.left, True)
    helper(root.right, False)


def ancestors(root, k):
    result = []
    ancestorsHelper(root, k, result, [])
    # print(result)
    return result


# # correct solution
#
# def ancestorsHelper(root, result, k):
#     if root is None:
#         return False
#     if root.data == k:
#         return True
#     if (ancestorsHelper(root.left, result, k) or ancestorsHelper(root.right, result,  k)):
#         result.append(root.data)
#         return True
#     return False


def ancestorsHelper(root, k, result, lst):
    if root is None:
        return result
    if root.data == k:

        result.append([*lst])
        # result = lst.copy()
    lst.append(root.data)
    if (root.left):
        ancestorsHelper(root.left, k, result, lst)
    if (root.right):
        ancestorsHelper(root.right, k, result, lst)
    lst.pop()


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k = int(input())
ans = ancestors(root, k)
print(ans[0])
