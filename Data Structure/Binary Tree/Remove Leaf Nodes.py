


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildLevelTree():

    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

def removeleafNodes(root):

    if root == None:
        return None
    if root.left == None and root.right== None:
        return None
    root.left = removeleafNodes(root.left)
    root.right = removeleafNodes(root.right)
    return root


def printpostorder(root):
    if root == None:
        return
    printpostorder(root.left)
    printpostorder(root.right)
    print(root.data ,end=" ")




# Main
root = buildLevelTree()
root = removeleafNodes(root)

printpostorder(root)

