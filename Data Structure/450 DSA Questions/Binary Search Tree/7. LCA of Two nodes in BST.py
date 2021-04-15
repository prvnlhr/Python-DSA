import BST


def LCA(root, n1, n2):
    if root is None:
        return None

    if root.data > n1 and root.data > n2:
        LCA(root.left, n1, n2)

    if root.data < n1 and root.data < n2:
        LCA(root.right, n1, n2)

    return root


root = BST.buildLevelTree()

n1 = int(input())
n2 = int(input())
ans = LCA(root, n1, n2)
print(ans.data)
