class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(head, n):
    og = head
    ptr = head
    count = 0
    while count < n:
        ptr = ptr.next
        count = count + 1
    # print(ptr.val)

    slow = ptr
    fast = ptr
    print(slow.val, fast.val)
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        print(slow.val, fast.val)

    print()
    print(slow.val, fast.val)


# Self Solved 100%
def clockwiseRotation(head, k):
    len = 1
    temp = head
    # step1:finding length____
    while (temp.next != None):
        len = len + 1
        temp = temp.next
    # print(len)
    #step2: checking k and length conditions___
    if (k > len):
        k = k % len
    k = len - k
    if (k == 0 or k == len):
        return head
    curr = head
    # step3: running loop to find kth element from last
    count = 1
    print('initial curr',curr.val)
    while (count < k and curr != None):
        print('c:', count, ',', 'k:', k, curr.val)
        curr = curr.next
        count = count + 1
    print(count, curr.val)
    if curr == None:
        return head

    # step4: making new connections
    nthListNode = curr
    # print()
    # print(nthListNode.val)

    temp.next = head
    head = nthListNode.next
    nthListNode.next = None
    return head


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
l = clockwiseRotation(l, n)
# solve(l, n)
printll(l)
