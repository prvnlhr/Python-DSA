import BST

p = [None]
q = [None]


def preSucc(root, key):
    global p
    global q

    if root is None:
        return

    preSucc(root.left, key)
    if root and root.data > key:
        # print(root.data)
        if ((not q[0]) or q[0] and q[0].data > root.data):
            q[0] = root
            print("q", q[0].data)
    elif root and root.data < key:
        p[0] = root
        print("p", p[0].data)
    preSucc(root.right, key)
    return p, q


root = BST.buildLevelTree()
key = 55
ans = preSucc(root, key)
print(ans[0][0].data, ans[1][0].data)
