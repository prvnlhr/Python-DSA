class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# O(n)__MY SOL 100%
def lastNthToFirst(head, n):
    sentinal = ListNode(0)
    sentinal.next = head
    prev = sentinal
    curr = sentinal.next
    ptr = curr
    for i in range(1, n):
        ptr = ptr.next

    while ptr.next:
        prev = curr
        curr = curr.next
        ptr = ptr.next
    if curr == head:
        return curr
    prev.next = curr.next
    curr.next = head
    head = curr
    return head


# O(n)
def lastNthToFirst(head, n):
    ptr = head
    nthRef = head
    count = 1
    while count < n:
        count = count + 1
        ptr = ptr.next
    nthPrev = nthRef
    while ptr.next:
        print(ptr.val, nthRef.val, nthPrev.val)
        nthPrev = nthRef
        nthRef = nthRef.next
        ptr = ptr.next
    print(nthPrev.val, nthRef.val, ptr.val)
    if nthRef.next:
        nthPrev.next = nthRef.next
    else:
        nthPrev.next = None
    nthRef.next = head
    head = nthRef
    return head


def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = ListNode(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    # print(None)
    return


# Program to detect loop and remove if exist
head = takeInput()
n = int(input())
newll = lastNthToFirst(head, n)
# print(newll.val)
printLL(newll)
