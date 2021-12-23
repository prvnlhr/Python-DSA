result = []


def rightViewHelper(root, level, max_level):
    global result
    if root is None:
        return []
    # check if next level is next level
    if max_level[0] < level:
        result.append(root.data)
    # update max_level
    max_level[0] = level
    rightViewHelper(root.right, level + 1, max_level)
    rightViewHelper(root.left, level + 1, max_level)


def rightView(root):
    result = []
    max_level = [0]
    level = 1
    rightViewHelper(root, level, max_level)
    return result
