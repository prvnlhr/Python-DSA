def diameterofBinaryTree(root):
    if root==None:
        return  0
    leftD = diameterofBinaryTree(root.left)
    rightD = diameterofBinaryTree(root.right)

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    H = leftHeight + rightHeight + 1
    value = max(H , leftD , rightD)
    return value

def height(root):
    if root ==None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    finalHeight = 1 + max(leftHeight , rightHeight)
    return finalHeight
