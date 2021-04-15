# Uses Extra second Stack
def reverseStack(s1, s2):
    if len(s1) <= 1:
        return
    lastElement = s1.pop()
    reverseStack(s1, s2)
    while len(s1) != 0:
        a = s1.pop()
        s2.append(a)
    s1.append(lastElement)
    while len(s2) != 0:
        b = s2.pop()
        s1.append(b)


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1, s2)
while (len(s1) != 0):
    print(s1.pop(), end=' ')
