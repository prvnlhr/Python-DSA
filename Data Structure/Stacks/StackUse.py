from StackUsingArray import Stack

s = Stack()
s.push(13)
s.push(12)
s.push(11)
s.push(10)
s.push(9)
s.push(8)
while s.isEmpty() is False:
    print(s.pop() , end=" ")
print()

print(s.pop())

print(s.isEmpty())
s.push(1)
s.push(2)
print(s.size())
print(s.isEmpty())

