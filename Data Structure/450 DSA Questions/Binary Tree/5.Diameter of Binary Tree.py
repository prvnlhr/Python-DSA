import BinaryTreeInputPrint

# The diameter of a tree can be defined as the maximum
# distance between two leaf nodes.
# Here, the distance is measured in terms of the total
# number of nodes present along the path of the two leaf nodes, including both the leaves.
#
# The diameter of a tree T is the largest of the following quantities:
# __the diameter of T’s left subtree.
# __the diameter of T’s right subtree.
# __the longest path between leaves that goes,
# __through the root of T (this can be computed from the heights of the subtrees of T)
#
# Leetcode Sol O(n):

ans = 1


def depth(root):
    global ans
    if root is None:
        return 0

    l = depth(root.left)
    r = depth(root.right)
    ans = max(ans, l + r + 1)
    return max(l, r) + 1


# __________OR____________________________
def dia(root):
    ans = 1

    def depth(root):
        global ans
        if root is None:
            return 0

        l = depth(root.left)
        r = depth(root.right)
        ans = max(ans, l + r + 1)
        return max(l, r) + 1

    depth(root)
    return ans - 1


# _________________________________________________
def heightTree(root, ans):
    if root == None:
        return 0
    lh = heightTree(root.left, ans)
    rh = heightTree(root.right, ans)
    ans[0] = max(ans[0], 1 + lh + rh)
    return 1 + max(lh + rh)


# Optimised O(n)____
def diameterOfTree(root):
    if root == None:
        return 0
    ans = [-999999]
    heightOfTree = heightTree(root, ans)
    return ans[0]


# ___________________________________________________
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)


# O(n^2)___
def diameter(root):
    lhMax = height(root.left)
    rhMax = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    h = lhMax + rhMax + 1
    dia = max(h, rd, ld)
    return dia


# Main____________________________________________________________________
BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = dia(root)
print(ans)
