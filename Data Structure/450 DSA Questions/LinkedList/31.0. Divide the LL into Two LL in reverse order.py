class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Self Solved
def DivideIntoTwo(head):
    # A = Node(None)
    # B = Node(None)
    A = None
    B = None
    flag = 'A'
    while (head != None):
        if flag == 'A':
            ptr = Node(head.data)
            ptr.next = A
            A = ptr
            flag = 'B'
        else:
            ptr = Node(head.data)
            ptr.next = B
            B = ptr
            flag = 'A'

        head = head.next

    printll(A)
    printll(B)


# _Main________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = DivideIntoTwo(l)
