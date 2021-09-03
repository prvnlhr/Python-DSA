# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Take Input____________________________________________________________________________________________________________
def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head is None:
            head = newNode

        else:
            curr = head

            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end='-->')
        curr = curr.next
    print("None")


def addPlusOneAlternative(head):
    temp = head
    while temp:
        print("curr", temp.data)
        temp.data = temp.data + 1
        print("curr new", temp.data)
        temp = temp.next.next
        print("curr.next", temp.data)

    print("After change")
    printLL(head)


def deleteithNode(head, i):
    count = 0
    prev = head
    curr = head

    if (i == 0):
        head = head.next
        return head

    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    print(prev.data, curr.data, count)

    if (curr.next is None):
        prev.next = None
    else:
        prev.next = curr.next

    return head


# __Main Driver Function_________________________________________________________________________________________________________________
head = takeInput()
i = int(input())
newHead = deleteithNode(head, i)
# addPlusOneAlternative(head)
printLL(newHead)
