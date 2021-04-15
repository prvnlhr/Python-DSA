import queue

def printLevelATNewLine(root):

    if root==None:
        return
    inputInQueue = queue.Queue()
    outputfromQueue = queue.Queue()
    inputInQueue.put(root)
    while not inputInQueue.empty():
        while not inputInQueue.empty():
            curr = inputInQueue.get()
            print(curr.data , end=' ')
            if curr.left!=None:
                outputfromQueue.put(curr.left)
            if curr.right!=None:
                outputfromQueue.put(curr.right)
        print()
        inputInQueue , outputfromQueue = outputfromQueue , inputInQueue
