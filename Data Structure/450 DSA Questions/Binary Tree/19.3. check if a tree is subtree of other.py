import BinaryTreeInputPrint


class Solution:
    # O(m + n)
    # m --> num of node of root1 and n--> num of nodes of root2
    def checkSubtreeOrNot(self, root1, root2):
        def getString(root):
            return '^' + str(root.data) + '#' + getString(root.left) + getString(root.right) if root else '$'

        s1 = getString(root1)
        s2 = getString(root2)
        return s2 in s1


BT = BinaryTreeInputPrint
root1 = BT.buildLevelTree()
root2 = BT.buildLevelTree()
ob = Solution()
ans = ob.checkSubtreeOrNot(root1, root2)
print(ans)
