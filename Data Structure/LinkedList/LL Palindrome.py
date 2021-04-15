from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


# Following is the ListNode class already written for the Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# solution 1 (Naive):_____________________________________________________________________________________
# we can take first element and traverse the whole LL to last element and compare them. In second iteration we
# can take second element and compare it with second last element by traversing to second last element.
# This would give time-complexity of O(n^2)
#
# solution 2:_____________________________________________________________________________________
# we could maintain a new head and reverse the whole linked list and then compare both.
# This we give time-complexity of O(n) and space-complexity O(n).
#
# solution 3: Better Approach_____________________________________________________________________
# we can find the midpoint and then we can divide the LL into two parts, first half and second half.
# now we can reverse only second half and compare it with first half
# This would give time-complexity of O(n) but space-complexity of O(1)

def reverse(head):
    curr = head
    prev = None
    fwd = None

    while curr is not None:
        fwd = curr.next
        curr.next = prev
        prev = curr
        curr = fwd
    return prev


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    fast = head
    slow = head
    # finding middle ListNode
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    # Making Second LL from midpoint and reversing
    secondHead = slow.next
    slow.next = None
    secondHead = reverse(secondHead)

    # traversing both first and second LL and comparing elements for equality
    firstSubList = head
    secondSubList = secondHead

    while firstSubList is not None:
        if firstSubList.val != secondSubList.val:
            return False

        firstSubList = firstSubList.next
        secondSubList = secondSubList.next

    firstSubList = head
    secondSubList = reverse(secondHead)

    while firstSubList.next is not None:
        firstSubList = firstSubList.next
    firstSubList.next = secondSubList

    return True


# MAIN_____

# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    vals = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(vals)) and (vals[i] != -1):
        val = vals[i]
        newListNode = ListNode(val)

        if head is None:
            head = newListNode
            tail = newListNode

        else:
            tail.next = newListNode
            tail = newListNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1
