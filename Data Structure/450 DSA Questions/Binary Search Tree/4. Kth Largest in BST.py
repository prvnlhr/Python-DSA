import BST

count = 0


# Traversing in reverse inOrder
def kthLargest(root, k):
    global count
    if root is None:
        return

    kthLargest(root.right, k)

    count = count + 1
    if count == k:
        print(root.data)

    kthLargest(root.left, k)


root = BST.buildLevelTree()
k = int(input())
ans = kthLargest(root, k)
