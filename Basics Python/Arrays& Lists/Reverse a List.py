def reverseList(li):
    l = len(li)
    for i in range(l//2):
        li[i], li[l - i - 1] = li[l - i - 1], li[i]



def reverseListNegativeIndexing(li):
    for i in range(len(li)//2):
        li[i], li[-1] = li[-1], li[i]


li = [int(i) for i in input().split()]
# reverseList(li)
reverseListNegativeIndexing(li)
print(li)
