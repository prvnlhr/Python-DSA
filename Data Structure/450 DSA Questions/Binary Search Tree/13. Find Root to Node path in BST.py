import BST

# Given a BST and an integer k. Find and return the path
# from the node with data k and root (if a node with data k
# is present in given BST) in a list. Return empty list otherwise.
# Note: Assume that BST contains all unique elements.

# Sample Input 1:
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# node = 2
# Sample Output 1:
# 2 5 8

result = []


def findPath(root, node):
    if root is None:
        return None
    # if root == node
    # create a path array and append root
    if root.data == node:
        path = []
        path.append(root.data)
        return path
    # if root > node,then find path in left subtree
    # if path found is and is not none
    # append it to path array an d return
    elif node < root.data:
        path = findPath(root.left, node)
        if path is not None:
            path.append(root.data)
        return path
    # if root < node ,  then find path in right subtree
    # if path is found and is not none
    # append it to path array an d return
    else:
        path = findPath(root.right, node)
        if path is not None:
            path.append(root.data)
        return path


root = BST.buildLevelTree()
node = int(input())
ans = findPath(root, node)
