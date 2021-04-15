import queue

# s = [1, 2 , 3 , 4 , 5 ]
# s.append(4)
# s.append(5)
#
# print(s.pop())
# print(s.pop())

# inbuilt queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.el̥mpty():
    print(q.get())


# inbuilt stack
s = queue.LifoQueue()
s.put(1)
s.put(2)
s.put(3)

while not s.empty():
    print(s.get())
