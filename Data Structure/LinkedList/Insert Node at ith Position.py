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


def insertAtith(head, i, element):
    count = 1
    temp = head
    prev = Node(None)
    newNode = Node(element)
    if i == 0:
        newNode.next = head
        head = newNode
        return head

    while temp is not None:

        if count == i:
            newNode.next = temp.next
            temp.next = newNode
            return head

        temp = temp.next
        count = count + 1
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
element = int(input())
newLL = insertAtith(head, i, element)
printLL(newLL)
