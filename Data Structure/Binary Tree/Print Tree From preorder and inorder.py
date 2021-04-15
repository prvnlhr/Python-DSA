def buildTreePreOrder(preorder , inorder):
    preLength = len(preorder)
    inLength = len(inorder)
    if preLength!= inLength or preorder==None or inorder==None or preLength==0:
        return None
    root = BinaryTreeNode(preorder[0])
    rootIndex = inorder.index(root.data)
    root.left = buildTreePreOrder(preorder[1:rootIndex+1] ,inorder[:rootIndex] )
    root.right = buildTreePreOrder(preorder[rootIndex+1:] , inorder[rootIndex+1:])
    return root

def buildTreePostOrder(postorder , inorder):
    postLength = len(postorder)
    inLegth = len(inorder)
    if postLength!=inLegth or postorder ==None or inorder==None or postLength==0:
        return None
    root = BinaryTreeNode(postorder[-1])
    rootIndex = inorder.index(root.data)
    root.left = buildTreePostOrder(postorder[:rootIndex] , inorder[:rootIndex])
    root.right = buildTreePostOrder(postorder[rootIndex:-1], inorder[rootIndex+1:])
    return root

