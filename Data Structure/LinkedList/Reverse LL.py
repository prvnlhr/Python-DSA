class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# RECURSIVE SOLUTION_____________________________________________________________________________________

def reverseRecursive(head):
    if head is None or head.next is None:
        return head

    smallHead = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return smallHead


def reverseIterative(head):
    if head == None:
        return None
    elif head.next == None:
        return head
    prev = head
    curr = prev.next
    next = curr.next

    prev.next = None
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
    curr.next = prev
    return curr


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
from sys import setrecursionlimit

setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)
