def KReverse(head, n):
    if (head == None or n <= 1):
        return head
    elif (head.next == None):
        return head

    prev = head
    curr = prev.next
    i = 1
    prev.next = None

    while curr and i < n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i = i + 1
    head.next = KReverse(curr, n)
    return prev

