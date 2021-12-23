
def swap_nodes(head , i , j):
    curr = head
    prev = previ = curri = prevj = currj = None
    count = 0
    while curr!=None:
        if count==i:
            previ = prev
            curri = curr
        elif count==j:
            prevj = prev
            currj = curr
        prev = curr
        curr = curr.next
        count = count+1
    if curri==None or currj==None:
        return
    if previ==None:
        head = currj
    else:
        previ.next = currj
    if prevj==None:
        head = curri
    else:
        prevj.next = curri
    curr = curri.next
    curri.next = currj.next
    currj.next = curr

    return head

