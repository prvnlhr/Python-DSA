from sys import stdin


def findTriplet(arr, n, x):
    paircount = 0
    for i in range(n):
        for j in range((i + 1), n):
            for k in range((j + 1), n):
                if (arr[i] + arr[j] + arr[k] == x):
                    paircount = paircount + 1
    print(paircount)


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    findTriplet(arr, n, x)
    print()

    t -= 1
