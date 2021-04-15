class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for i in range(n + 1):
        print(first.val)
        first = first.next
    print()
    print(first.val)

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


# _Main________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    last = head
    for val in arr[1:]:
        last.next = ListNode(val)
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
n = int(input())
head = removeNthFromEnd(l, n)
(printll(head))
