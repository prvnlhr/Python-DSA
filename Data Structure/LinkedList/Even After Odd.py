# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def arrange_LinkedList(head):
    if head is None:
        return head
    even = None
    oddHead = None

    while head:
        next = head.next
        if head.data % 2 == 0:
            if even == None:
                even = head
                evenTail = head
            else:
                evenTail.next = head
                evenTail = head
        else:
            if oddHead == None:
                oddHead = head
                oddTail = head
            else:
                oddTail.next = head
                oddTail = head

        head.next = None
        head = next
    if oddHead == None:
        return even
    oddTail.next = even
    return oddHead




def ll(arr):
    if len(arr)==0:
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
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)
