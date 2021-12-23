class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Geeks for Geeks Solution:
def reorderList(head):
    if (head is None):
        return None

    temp = head
    ans = []

    while head:
        ans.append(head)
        head = head.next

    if (len(ans) == 1 or len(ans) == 2):
        return temp

    prev = temp
    curr = prev.next
    len_ = len(ans)

    if (len_ % 2 == 0):
        act_ = len_ // 2 - 1

    else:
        act_ = len_ // 2 + 1

    while act_ > 0:
        n = ans.pop()
        n.next = None
        prev.next = n
        prev.next.next = curr
        prev = curr
        curr = curr.next
        act_ -= 1

    curr.next = None

    return head


# CN Solution
def rearrange(head):
    if (head == None):
        return head
    second = head.next
    prev = second
    if (prev == None):
        return head
    last = prev.next
    if (last == None):
        return head
    # atleast 3 node are present
    while (last.next):
        prev = last
        last = last.next
    #

    head.next = last
    prev.next = None
    last.next = rearrange(second)
    return head


# LeetCodeSolution O(N)
def reorderList(head):
    if head is None or head.next is None:
        return head

    # Calculate the length of the list
    list_len = 0
    cur = head
    while cur is not None:
        list_len += 1
        cur = cur.next

    # Splice the list into the first floor(n/2) nodes and the last ceiling(n/2) nodes
    aux = Node(head)
    l1 = aux
    l2 = head
    for i in range(list_len // 2):
        l1 = l1.next
        l2 = l2.next
    l1.next = None
    l1 = head

    # Reverse the last ceiling(n/2) nodes
    l2 = rev_list(l2)

    # Interleave the two lists
    res = Node(head)
    cur = res

    while l1 is not None and l2 is not None:
        cur.next = l1
        l1 = l1.next
        cur = cur.next
        cur.next = l2
        l2 = l2.next
        cur = cur.next
        cur.next = None

    if l2 is not None:
        cur.next = l2
    return res.next

    # print(l1, "\n", l2)


def rev_list(Node):
    if head is None or head.next is None:
        return head

    res = Node(None)
    cur = head

    while cur is not None:
        tmp = cur.next
        cur.next = None
        tmp2 = res.next
        res.next = cur
        cur.next = tmp2
        cur = tmp
    return res.next


# __MAIN__________________________________________________________________________________________
# TakeInput
def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


head = takeInput()
reorderList(head)
printLL(head)
