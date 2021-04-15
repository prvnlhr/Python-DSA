def SwapAlternate(li, n):
    for i in range(0, n - 1, 2):
        print(li[i])
        li[i], li[i + 1] = li[i + 1], li[i]


n = int(input())
li = [int(i) for i in input().split()]

SwapAlternate(li, n)
print(li)
