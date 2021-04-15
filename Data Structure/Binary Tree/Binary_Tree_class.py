# _TAKING INPUT AND CREATING A BINARY TREE CLASS__________________________________________________________________________
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintTree(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data, end=" ")
    print()
    PrintTree(root.left)
    PrintTree(root.right)


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftree = takeInput()
    righttree = takeInput()
    root.left = leftree
    root.right = righttree
    return root


# _______________________________________________________________________________________________________________________
# _MAIN DRIVER FUNCTION:-------------------------------------------------------------------------------------------------


# #_1_.count No of Nodes in Binary Tree Program___________________________________________________________________________
# def NumNodes(root):
#     if root == None:
#         return 0
#     leftcount = NumNodes(root.left)
#     rightcount = NumNodes(root.right)
#     return 1 + leftcount + rightcount
#
# root = takeInput()
# numberofNodes = NumNodes(root)
# print("No. of Nodes :" , numberofNodes)

# _2_.Sum of Nodes_______________________________________________________________________________________________________
# def SumofNodes(root):
#     if root == None:
#         return 0
#
#     leftsum = SumofNodes(root.left)
#     rightsum = SumofNodes(root.right)
#     return root.data + leftsum + rightsum
#
#
# root = takeInput()
# sum = SumofNodes(root)
# print(sum)
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False


root = takeInput()
PrintTree(root)
ans = isBalanced(root)
print(ans)
