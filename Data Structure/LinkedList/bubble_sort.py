def bubble_sort(head):

    if head==None or head.next==None:
        return head
    swap = True
    while swap:
        swap = False
        prev = None
        curr = head
        next = curr.next
        while next:
            if curr.data > next.data:
                swap =True
                if prev :
                    prev.next = next
                else:
                    head = next
                curr.next = next.next
                next.next = curr
                prev = next
            else:
                prev = curr
            curr = prev.next
            next = curr.next
    return  head

