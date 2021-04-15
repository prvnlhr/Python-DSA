# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# optimise O(n) : By maintaining tail to avoid  traversing again and again from head to last node_______________________
def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


def DeleteAtith(head, i):
    if head is None:
        return head
    if i == 0:
        return head.next
    count = 0
    curr = head
    while curr is not None and count < (i - 1):
        count = count + 1
        curr = curr.next
    if (curr is None) or (curr.next is None):
        return head
    curr.next = curr.next.next
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print(None)
    return


# __Main Driver Function_________________________________________________________________________________________________________________
head = takeInput()
i = int(input())
newLL = DeleteAtith(head, i)
printLL(newLL)
