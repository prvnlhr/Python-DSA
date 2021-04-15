###Following Node class us already created internally. You can directly use that.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLL:

    def __init__(self):
        self.head = None
        self.size = 0

    # Push_______________________________
    # we insert new Node at start unlike LL in which we append to last so that we can delete element at O(1)
    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    # pop________________________________
    def pop(self):

        if self.isEmpty() is True:
            return 0
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp

    def top(self):
        if self.isEmpty() is True:
            return 0
        else:
            return self.head.data

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size


s = StackUsingLL()
li = [int(ele) for ele in input().split()]
i = 0
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i + 1])
        i += 1
    elif choice == 2:
        ans = s.pop()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        if (s.isEmpty()):
            print('true')
        else:
            print('false')
    i += 1
