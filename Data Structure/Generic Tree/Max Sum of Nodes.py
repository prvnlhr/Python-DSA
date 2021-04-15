class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    # _______________________________________________________________________________________________________________________
    def sum(self):
        ans = self.data
        for child in self.children:
            ans = ans + child.data
        return ans


# CN sol__________________
def maxSum(tree):
    if tree == None:
        return None
    ans, ansSum = tree, tree.sum()
    for child in tree.children:
        temp, tempSum = maxSum(child)
        if tempSum > ansSum:
            ans, ansSum = temp, tempSum
    return ans, ansSum
# _______________________________________________________________________________________________________________________


def maxSumUtil(root, resNode, maxsum):
    # Base Case
    if root == None:
        return

    # curr contains the sum of the root
    # and its children
    currsum = root.data

    # total no of children
    count = len(root.children)

    # for every child call recursively
    for i in range(0, count):
        currsum += root.children[i].data
        resNode, maxsum = maxSumUtil(root.children[i], resNode, maxsum)

    # if curr is greater than sum,
    # update it
    if currsum > maxsum:
        # resultant node
        resNode = root
        maxsum = currsum

    return resNode, maxsum


# Function to find the node having
# max sum of children and node
def maxSumNode(root):
    # resultant node with max
    # sum of children and node
    resNode, maxsum = None, 0
    resNode, maxsum = maxSumUtil(root, resNode, maxsum)

    # return the key of resultant node
    return resNode, maxsum


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)
