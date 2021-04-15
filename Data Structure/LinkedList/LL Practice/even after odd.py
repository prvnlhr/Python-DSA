# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# NOTE: We are not arrange on basis of list values, we are arranging on basis of even and odd positions
def arrange_LinkedList(head):
    # Steps: 1.we will maintain odd and even list
    # 2.we will connect even places to even list and odd places to odd list
    # 3.finally we will connect even list after odd list
    # Corner case
    if (head == None):
        return None

    # Initialize first nodes of
    # even and odd lists
    odd = head
    even = head.next

    # Remember the first node of even list so
    # that we can connect the even list at the
    # end of odd list.
    evenFirst = even

    # infinite loop
    while (1 == 1):

        # If there are no more nodes,
        # then connect first node of even
        # list to the last node of odd list
        if (odd == None or even == None or (even.next) == None):
            odd.next = evenFirst
            break

        # Connecting odd nodes
        odd.next = even.next
        # updating odd
        odd = even.next

        # If there are NO more even nodes
        # after current odd.
        if (odd.next == None):
            even.next = None
            odd.next = evenFirst
            break

        # Connecting even nodes
        even.next = odd.next
        # updating even
        even = odd.next
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
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)
