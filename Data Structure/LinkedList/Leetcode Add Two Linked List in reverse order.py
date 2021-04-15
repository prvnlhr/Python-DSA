class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# 100% self Solved
def addTwoNumbers(head1, head2):
    ptr1 = head1
    ptr2 = head2
    newLL = None
    tail = None
    carry = 0

    while ptr1 or ptr2:

        if ptr1 and ptr2:
            addition = ptr1.val + ptr2.val
        elif ptr1:
            addition = ptr1.val
        elif ptr2:
            addition = ptr2.val

        newData = (addition + carry) % 10
        # if ptr1 and ptr2:
        #     print('ptr1:', ptr1.val, 'ptr2:', ptr2.val, 'addition:', addition, 'carry:', carry, 'newData:', newData)
        # elif ptr1:
        #     print('ptr1:', ptr1.val, 'carry:', carry, 'addition:', addition, 'carry:', carry, 'newData:', newData)
        # elif ptr2:
        #     print('ptr2:', ptr2.val, 'carry:', carry, 'addition:', addition, 'carry:', carry, 'newData:', newData)

        NewNode = Node(newData)

        if newLL == None:
            newLL = NewNode
            tail = NewNode
        else:

            tail.next = NewNode
            tail = NewNode

        carry = (addition + carry) // 10
        # print('add', addition + carry, 'carr', carry)

        if ptr1:
            ptr1 = ptr1.next
        if ptr2:
            ptr2 = ptr2.next

    if carry > 0:
        NewNode = Node(carry)
        tail.next = NewNode
        tail = NewNode

    return newLL


def printll(head):
    while head:
        print(head.val, end=' ')
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


head1 = takeInput()
head2 = takeInput()
newLL = addTwoNumbers(head1, head2)
printll(newLL)
