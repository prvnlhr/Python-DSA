class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def midpoint_linkedlist(head):
#     slow = head
#     fast = head
#     while fast.next.next is not None:
#         if fast.next is None:
#             return slow
#
#         slow = slow.next
#         fast = fast.next.next
#     return slow

def length(head):
    temp = head
    count = 1
    while (temp.next != None):
        count = count + 1
        temp = temp.next

    return count


def getMiddle(head):
    slow = head
    fast = head
    if (head == None):
        return head

    if (length(head) % 2 == 0):
        while (fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        middle = slow

    else:
        while (fast.next != None):
            slow = slow.next
            fast = fast.next.next

    middle = slow
    return middle


def mergeSort(head):
    if head is None or head.next is None:
        return head
    head1 = head
    mid = getMiddle(head)
    head2 = mid.next
    mid.next = None

    return MergeTwoList(mergeSort(head1), mergeSort(head2))


def MergeTwoList(head1, head2):
    t1 = head1
    t2 = head2
    head = None
    tail = None

    if t1.val <= t2.val:
        head = t1
        tail = t1
        t1 = t1.next
    else:
        head = t2
        tail = t2
        t2 = t2.next

    while t1 is not None and t2 is not None:
        if t1.val <= t2.val:
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
    for val in arr[1:]:
        last.next = Node(val)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
