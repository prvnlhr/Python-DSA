from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


count = 0

#Length Function_________________________________________________
def length(head):
    global count
    temp = head
    while temp is not None:
        count = count + 1
        temp = temp.next
    return count

# __________________________________________________
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


# to print the linked list_____________________________________
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main______________________________________________
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    print(length(head))

    t -= 1
