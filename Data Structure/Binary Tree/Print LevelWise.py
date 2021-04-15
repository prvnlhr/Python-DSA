import queue
def PrintLevelWise(root):

    if root ==None:
        return
    q = queue.Queue()
    q.put(root)

    while(not q.empty()):
        curr = q.get()
        currData = curr.data
        left = -1
        right = -1
        if curr.left != None :
            left = curr.left.data
            q.put(curr.left)
        if curr.right != None:
            right = curr.right.data
            q.put(curr.right)

        print(currData, ":L:" ,left , "R:" ,right , sep='')


