import BST


# 1. Initialize current as root
# 2. While current is not NULL
#    If the current does not have left child
#       a) Print current’s data
#       b) Go to the right, i.e., current = current->right
#    Else
#       a) Find rightmost node in current left subtree OR node whose right child == current.
#          If we found , right child == current
#              a) Update the right child as NULL of that node whose right child is current
#              b) Print current’s data
#              c) Go to the right, i.e. current = current->right
#          Else
#              a) Make current as the right child of that rightmost
#                 node we found; and
#              b) Go to this left child, i.e., current = current->left

def morrisInorderTraversal(root):
    sol = []

    curr = root

    while curr is not None:  # This Means we have reached Right Most Node i.e end of LDR traversal
        if curr.left is not None:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                sol.append(curr.data)
                pre.right = None
                curr = curr.right
        else:
            sol.append(curr.data)
            curr = curr.right

    return sol


root = BST.buildLevelTree()
ans = morrisInorderTraversal(root)
print(ans)
