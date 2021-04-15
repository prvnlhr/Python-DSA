class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findTheNodeofLoop(head , start , end):

    n = start-end
    count = 1
    if(n == 0):
        return None
    while(count < n ):
        head = head.next
        count = count + 1
    # print(head.data)
    return head.data


#    4 OUT OF 6 cases passed codeZen




#__Main_____________________________________________________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
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
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
a = int(input())
b = int(input())
l = findTheNodeofLoop(l, a , b)
print(l)
# printll(l)
