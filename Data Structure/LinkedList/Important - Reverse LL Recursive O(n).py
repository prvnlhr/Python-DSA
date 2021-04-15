from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#_______________________________________________________________________________________________________________________
def ReverseRec(head):

    if head is None or head.next is None:
        return head
    smallhead = ReverseRec(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead
#_______________________________________________________________________________________________________________________

def ReverseIt(head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head
#_______________________________________________________________________________________________________________________

# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    head = ReverseRec(head)
    printLinkedList(head)

    t -= 1

