def stockSpan(price, n):
    s = []
    span = []
    s.append(0)
    span.append(1)
    l = len(price)
    for i in range(1, l):
        print(s[-1])
        while (len(s) != 0 and price[s[-1]] < price[i]):
            s.pop()
        if len(s) == 0:
            span.append(i + 1)
        else:
            span.append(i - s[-1])
        s.append(i)
    return span


n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price, n)
for ele in spans:
    print(ele, end=' ')
