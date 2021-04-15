def printOneToN(n):
    if (n == 1):
        print(n)
        return

    printOneToN(n-1)
    print(n)


n = int(input())
printOneToN(n)
