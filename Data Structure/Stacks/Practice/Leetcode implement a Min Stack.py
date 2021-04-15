import sys


# class MinStack:
#
#     def __init__(self):
#         self.stack = []
#         self.min = float('inf')
#
#     def push(x: int) -> None:
#         self.min = min(self.min, x)
#         self.stack.append((x,self.min))
#
#     def pop(self) -> None:
#         self.stack.pop()
#         try:
#             self.min = self.stack[-1][1]
#         except:
#             self.min = float('inf')
#
#     def top(self) -> int:
#         return self.stack[-1][0]
#
#     def getMin(self) -> int:
#         return self.stack[-1][1]

class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = sys.maxsize
        self.size = 0

    def push(self, x):
        # if we don't change  self.Min in pop() func after popping an element then we have to write all
        # this extra line of code
        #
        # # print('push', x)
        # if self.size == 0:
        #         self.Min = x
        #         self.stack.append((x, self.Min))
        # else:
        #     currMin = self.getMin()
        #     # print('currMin:', currMin, ',','x:', x)
        #     if x < currMin:
        #         self.Min = x
        #         self.stack.append((x, x))
        #     else:
        #         self.stack.append((x, currMin))
        # self.size = self.size + 1
        # print(self.stack, ',', 'top', self.top(), ',', 'min', self.getMin())
        #
        # Simplified:_______after changing the self.Min value in pop() func , after popping an element
        self.Min = min(x, self.Min)
        self.stack.append((x, self.Min))
        self.size = self.size + 1

    def pop(self):
        # print('pop')
        if self.size == 0:
            return None
        self.stack.pop()
        self.size = self.size - 1
        # after popping changing the self.Min (All the trick lies here)
        if self.size == 0:
            self.Min = sys.maxsize
        else:
            self.Min = self.stack[-1][1]
        # print(self.stack, ',', 'top', self.top(), ',', 'min', self.getMin())

    def top(self):
        if self.size == 0:
            return None
        return self.stack[-1][0]

    def getMin(self):
        if self.size == 0:
            return None
        return self.stack[-1][1]


minStack = MinStack()
# minStack.push(2147483646)
# minStack.push(2147483646)
# minStack.push(2147483647)
# minStack.stack)
#  minStack.top()  # return 0
# minStack.pop()
# minStack.stack)
#  minStack.getMin()  # return -3
# minStack.pop()
# minStack.stack)
#  minStack.getMin()  # return -3
# minStack.pop()
# minStack.stack)
# minStack.push(2147483647)
#  minStack.top()
#  minStack.getMin()  # return -3
# minStack.push(-2147483648)
# minStack.stack)
#  minStack.top()
#  minStack.getMin()  # return -2
# minStack.pop()
# minStack.stack)
#  minStack.getMin()  # return -2
# minStack.stack)

# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.push(-1)
# minStack.push(-3)
# minStack.pop()
# minStack.pop()
# minStack.pop()
# minStack.pop()
# minStack.push(10)
# minStack.stack)
# minStack.getMin()
# minStack.pop()
# minStack.stack)
# minStack.top()
# minStack.stack)
# minStack.getMin()

minStack.push(-10)
minStack.push(14)
print('min', minStack.getMin())
print('min', minStack.getMin())
minStack.push(-20)
print('min', minStack.getMin())
print('min', minStack.getMin())
print('top', minStack.top())
print('min', minStack.getMin())
minStack.pop()
minStack.push(10)
minStack.push(-7)
print('min', minStack.getMin())
minStack.push(-7)
minStack.pop()
print('top', minStack.top())
print('min', minStack.getMin())
minStack.pop()
