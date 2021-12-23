import queue
import sys
import BinaryTreeInputPrint


def topView(root):
    map = {}
    minEle = sys.maxsize

    if root is None:
        return None

    q = queue.Queue()
    q.put((root, 0))

    while not q.empty():
        curr = q.get()
        if curr[1] not in map:
            map[curr[1]] = curr[0].data
            minEle = min(minEle, curr[1])
        if curr[0].left:
            q.put((curr[0].left, curr[1] - 1))
        if curr[0].right:
            q.put((curr[0].right, curr[1] + 1))

    for minEle in map:
        print(map[minEle], end=' ')
        minELe = minEle + 1


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = topView(root)
