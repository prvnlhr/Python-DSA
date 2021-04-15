import BST
import sys


class isBSTReturn:
    def __init__(self, min, max, isBST):
        self.min = min
        self.max = max
        self.isBST = isBST


# O(n) worst case
def isBST(root):
    if root is None:
        return isBSTReturn(sys.maxsize, ~sys.maxsize, True)

    leftAns = isBST(root.left)
    rightAns = isBST(root.right)

    Min = min(root.data, min(leftAns.min, rightAns.min))
    Max = max(root.data, max(leftAns.max, rightAns.max))

    isBst = True

    if leftAns.max >= root.data:
        isBst = False

    if leftAns.isBST == False:
        isBst = False

    if rightAns.isBST == False:
        isBst = False

    ans = isBSTReturn(Min, Max, isBst)

    return ans


root = BST.buildLevelTree()

ans = isBST(root)
print(ans.isBST)
