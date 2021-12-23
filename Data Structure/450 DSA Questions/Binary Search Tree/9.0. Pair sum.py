import BST


# _CN_________________________________________________________________________________

def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


def printNodesSumToS1(root, s):
    if root == None:
        return
    totalNodes = countNodes(root)
    count = 0
    inorder = []
    revInorder = []
    temp = root
    while temp != None:
        inorder.append(temp)
        temp = temp.left
    temp = root
    while temp != None:
        revInorder.append(temp)
        temp = temp.right
    # for i in range(len(inorder)):
    #     print(inorder[i].data, end=" ")
    #     print()
    # for i in range(len(revInorder)):
    #     print(revInorder[i].data, end=" ")
    #     print()

    while count < totalNodes - 1:
        top1 = inorder.pop()
        top2 = revInorder.pop()
        inorder.append(top1)
        revInorder.append(top2)
        if top1.data + top2.data == s:
            print(top1.data, end=' ')
            # print(top2.data)
            top = top1
            # print(top.data)
            inorder.pop()
            count = count + 1
            if top.right != None:
                top = top.right
                while top != None:
                    inorder.append(top)
                    top = top.left
            top = top2
            revInorder.pop()
            count = count + 1
            if top.left != None:
                top = top.left
                while top != None:
                    revInorder.append(top)
                    top = top.right
        elif top1.data + top2.data > s:
            top = top2
            revInorder.pop()
            count = count + 1
            if top.left != None:
                top = top.left
                while top != None:
                    revInorder.append(top)
                    top = top.right
        else:
            top = top1
            inorder.pop()
            count = count + 1
            if top.right != None:
                top = top.right
                while top != None:
                    inorder.append(top)
                    top = top.left


# ___GeeksForGeeks 100% correct___________________________________________________________________
def printNodesSumToS2(root, s):
    d = set()
    sum = s
    findPair(root, sum, d)


def findPair(root, sum, set):
    # base case
    if root is None:
        return False

    # return true if pair is found in the left subtree else continue
    # processing the node
    if findPair(root.left, sum, set):
        return True

    # if pair is formed with current node, print the pair and return True
    if sum - root.data in set:
        print(sum - root.data, root.data)
        return True

    # insert current node's value into the set
    else:

        set.add(root.data)

    # search in right subtree
    return findPair(root.right, sum, set)


# _________________________________________________________________________________________

# Main
root = BST.buildLevelTree()
s = int(input())
printNodesSumToS1(root, s)
print()
# printNodesSumToS2(root, s)
