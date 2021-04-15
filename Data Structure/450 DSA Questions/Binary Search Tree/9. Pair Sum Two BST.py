import BST


# Given two BSTs containing n1 and n2 distinct nodes respectively. Given a value x.
# The problem is to count all pairs from both the BSTs whose sum is equal to
#
# Input : BST 1:    5
#                 /   \
#                3     7
#               / \   / \
#              2  4  6   8
#
#         BST 2:    10
#                 /   \
#                6     15
#               / \   /  \
#              3  8  11  18
#         x = 16
#
# Output : 3
# The pairs are:
# (5, 11), (6, 10) and (8, 8)

def countPairs(root1, root2, k):
    # base Condition:
    if root1 is None or root2 is None:
        return 0

    # Stack 'st1' used for the inorder
    # traversal of BST 1
    # stack 'st2' used for the reverse
    # inorder traversal of BST 2
    st1 = []
    st2 = []
    count = 0
    while 1:

        while root1 != None:
            st1.append(root1)
            root1 = root1.left
        while root2 != None:
            st2.append(root2)
            root2 = root2.right

        if (len(st1) == 0 or len(st2) == 0):
            break

        top1 = st1[len(st1) - 1]
        top2 = st2[len(st2) - 1]
        if top1.data + top2.data == k:
            count = count + 1
            st1.remove(st1[len(st1) - 1])
            st2.remove(st2[len(st2) - 1])

            root1 = top1.right
            root2 = top2.left


        elif ((top1.data + top2.data) < k):
            st1.remove(st1[len(st1) - 1])
            root1 = top1.right
        else:
            st2.remove(st2[len(st2) - 1])
            root2 = top2.left

    return count


root1 = BST.buildLevelTree()
root2 = BST.buildLevelTree()
k = int(input())
ans = countPairs(root1, root2, k)
print(ans)
