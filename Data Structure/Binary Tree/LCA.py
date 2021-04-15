import queue


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#


def findPath(root, path, k):
    # Base Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.data)

    # See if the k is same as root's data
    if root.data == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False


# Returns LCA if node node1 , node2 are present in the given
# binary tre otherwise return -1
def lcaOfThreeNodes(root, node1, node2, node3):
    # To store paths to node1 and node2 fromthe root
    path1 = []
    path2 = []
    path3 = []
    ans = None

    # Find paths from root to node1 and root to node2.
    # If either node1 or node2 is not present , return -1
    if (not findPath(root, path1, node1, ) or not findPath(root, path2, node2) or not findPath(root, path3, node3)):
        return -1
    # print(path1)
    # print(path2)
    # print(path3)

    # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2) and i < len(path3)):
        # print(print(path1[i], path2[i], path3[i]))
        a = path1[i]
        b = path2[i]
        c = path3[i]
        # print('a:', a, 'b:', b, 'c:', c)
        # if a == b:
            # print(a, b)
            # print('c,', c)
            # if b == c:
                # print(a, b, c)
        # print()
        # print('_______')
        if a == b == c:
            ans = a
        else:
            break
        i += 1
    return ans
            # print(a, b, c)
        # print()
        # print()

        # if a != b != c:
        #     print(a, b, c)
        #     break

        # if path1[i] != path2[i]:
        #     ans = path1[i]
        #     if path3[i] == ans:
        #         ans = path1[i]
        #     else:
        #         return path1[i - 1]

        # break

    # return ans


# ____________
#
# def Helper(root, node1, node2, node3, v):
#     if root is None:
#         return None
#
#     if root.data == node1:
#         v[0] = True
#         return root.data
#     if root.data == node2:
#         v[1] = True
#         return root.data
#     if root.data == node3:
#         v[2] = True
#         return root.data
#
#     leftLCA = Helper(root.left, node1, node2, node3, v)
#     rightLCA = Helper(root.right, node1, node2, node3, v)
#
#     if leftLCA and rightLCA:
#         return root.data
#
#     return leftLCA if leftLCA is not None else rightLCA
#
#
# def find(root, k):
#     if root is None:
#         return False
#
#     if root.data == k or find(root.left, k) or find(root.right, k):
#         return True
#
#     return False
#

# def lcaOfThreeNodes(root,node1,node2,node3):
#     v =[False,False]
#
#     lca = Helper(root,node1,node2,node3,v)
#
#     if v[0] and v[1] and v[2] or v[0] and find(lca,)

# def lcaOfThreeNodes(root, node1, node2, node3):
#     if root is None:
#         return None
#
#     if root.data == node1 or root.data == node2 or root.data == node3:
#         return root.data
#
#     leftLCA = lcaOfThreeNodes(root.left, node1, node2, node3)
#     rightLCA = lcaOfThreeNodes(root.right, node1, node2, node3)
#
#     if leftLCA and rightLCA:
#         return root.data
#
#     return leftLCA if leftLCA is not None else rightLCA


# Building the tree
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


t = int(input())
while t > 0:
    arr = [int(i) for i in input().split()][:3]
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(lcaOfThreeNodes(root, arr[0], arr[1], arr[2]))
    t = t - 1
