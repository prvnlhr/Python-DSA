INT_MIN = -2147483648
INT_MAX = 2147483647

def minMax(root):
    minimum , maximum = INT_MAX , INT_MIN

    if root ==None:
        return minimum , maximum
    leftMin , leftMax = minMax(root.left)
    rigthMin , rightMax = minMax(root.right)
    minimum = min(root.data , leftMin , rigthMin)
    maximum = max(root.data , leftMax , rightMax)
    return minimum , maximum
