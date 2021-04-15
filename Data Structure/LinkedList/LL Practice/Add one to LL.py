# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#
# def addOne(head):
#     if (head.next == None):
#         return head
#
#     smallHead = addOne(head.next)
#     print(smallHead.data)
#     head.next.data = head.next.data + 1
#     return head


def addWithCarry(head):
    # If linked list is empty, then
    # return carry
    if (head == None):
        return 1

    # Add carry returned be next node call
    res = head.data + addWithCarry(head.next)

    # Update data and return new carry
    head.data = int((res) % 10)
    return int((res) / 10)


# This function mainly uses addWithCarry().
def addOne(head):
    carry = addWithCarry(head)

    if (carry != 0):
        newNode = Node(0)
        newNode.data = carry
        newNode.next = head
        return newNode

    return head


# _Main_____________________________
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


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


# __Main Driver Function_________________________________________________________________________________________________________________
head = takeInput()
newLL = addOne(head)
printLL(newLL)
