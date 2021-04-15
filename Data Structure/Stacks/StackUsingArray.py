class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.data[len(self.data)]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0
