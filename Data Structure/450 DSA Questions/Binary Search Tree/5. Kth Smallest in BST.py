import BST

count = 0


# Traversing in reverse inOrder
def kthSmallest(root):
    global count
    global k

    if root is None:
        return

    left = kthSmallest(root.left)

    if left != None:
        return left
    k = k - 1

    if k == 0:
        return root

    return kthSmallest(root.right)


root = BST.buildLevelTree()
k = int(input())
ans = kthSmallest(root)
print(ans.data)
