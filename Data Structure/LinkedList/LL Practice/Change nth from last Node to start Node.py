class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ChangeStart(head, n):
    # print(n)
    ptr = head
    count = 1
    while (count < n):
        count = count + 1
        ptr = ptr.next
    required = head
    prev = required
    next = required.next
    # print(ptr.data , main.data)
    while (ptr.next is not None):
        # print(main.data , ptr.data)
        ptr = ptr.next
        prev = required
        required = required.next
        next = required.next

    print(prev.data , required.data , next.data)
    required.next = head
    prev.next = next
    head = required
    return head


# __Main_____________________________________________________________________________________________________________________
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
n = int(input())
l = ChangeStart(l, n)
printll(l)
