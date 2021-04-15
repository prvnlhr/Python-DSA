






def rootToLeafPathsSumToK(root, k, lst):
    if root == None:
        return
    if root.left == None and root.right == None:
        if root.data == k:
            print(*lst, k)
        return
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k - root.data.lst)
    rootToLeafPathsSumToK(root.right, k - root.data, lst)
    lst.pop()
