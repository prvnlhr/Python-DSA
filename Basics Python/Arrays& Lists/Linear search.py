def linearSearch(x, li):
    for i in range(len(li)):
        if (li[i] == x):
            return i
        else:
            return -1


x = int(input())
li = [int(i) for i in input().split()]
index = linearSearch(x, li)
print(index)
