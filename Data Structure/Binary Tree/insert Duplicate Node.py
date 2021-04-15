def insertDuplicatesNode(root):
    if root==None:
        return
    newNode = BinaryTreeNode(root.data)
    rootLeft = root.left
    root.left = newNode
    newNode.left = rootLeft
    insertDuplicatesNode(rootLeft)
    insertDuplicatesNode(root.right)
    
