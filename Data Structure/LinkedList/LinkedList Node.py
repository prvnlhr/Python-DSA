# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# __Main___________________________

a = Node(10)
b = Node(12)
a.next = b
print("a.data :", +a.data)
print("b.data :", b.data)
print("a.next.data:", a.data, "->", a.next.data)
