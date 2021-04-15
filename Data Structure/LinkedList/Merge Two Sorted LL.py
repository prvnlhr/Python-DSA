class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(head1, head2):
    t1 = head1
    t2 = head2
    head = None
    tail = None

    if t1.data <= t2.data:
        head = t1
        tail = t1
        t1 = t1.next
    else:
        head = t2
        tail = t2
        t2 = t2.next

    while t1 is not None and t2 is not None:
        if t1.data <= t2.data:
            tail.next = t1
            tail = t1
            t1 = t1.next

        else:
            tail.next = t2
            tail = t2
            t2 = t2.next
    # One list is empty Now
    if t1 is not None:
        tail.next = t1
    else:
        tail.next = t2
    return head


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
arr1 = list(int(i) for i in input().strip().split(' '))
arr2 = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)
