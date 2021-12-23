from sys import stdin


# Following is the ListNode class already written for the Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def ReverseIt(head, m, n):
    prev = None
    current = head
    pos = n - m
    count = 0
    initial = current
    while (current is not None):
        # print(count,pos)
        if count > pos:
            break
        next = current.next
        current.next = prev
        prev = current
        current = next
        count = count + 1
    head = prev
    # print('curr', current.val, 'prev', prev.val, initial.val)
    # prev.next = current
    initial.next = current
    # printLinkedList(head)
    # printLinkedList(current)
    return head


def reverseBetween(head, m, n):
    if n - m == 0:
        return head
    if m == 1:
        if n - m == 1:
            temp = head.val
            head.val = head.next.val
            head.next.val = temp
            return head

    ptr = head
    count = 1
    prev = None
    while ptr and count < m:
        prev = ptr
        ptr = ptr.next
        count = count + 1
    ll = ReverseIt(ptr, m, n)
    if prev:
        prev.next = ll
        return head
    else:
        return ll


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        val = datas[i]
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

head = takeInput()
m = int(input())
n = int(input())
newLL = reverseBetween(head, m, n)
printLinkedList(newLL)
