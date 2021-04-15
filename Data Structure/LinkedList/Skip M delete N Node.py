class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipMdeleteN(head, M, N):
    if M == 0:
        return None
    if N == 0:
        return head
    curr = head
    temp = None

    while curr != None:
        take = 0
        skip = 0
        while curr != None and take < M:
            if temp == None:
                temp = curr
            else:
                temp.next = curr
                temp = curr
            curr = curr.next
            take = take + 1
        while curr != None and skip < N:
            newNode = curr
            curr = newNode.next
            skip = skip + 1
    if temp != None:
        temp.next = None
    return head



def ll(arr):
    if len(arr)==0:
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
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l)
