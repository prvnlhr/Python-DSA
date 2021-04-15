def findWinner(N, x, y):


    if N == 1:
        return 'Beerus'
    if N == x:
        return 'Beerus'
    if N == y:
        return "Beerus"
    else:
        findWinner(N - 1, x, y )
        findWinner(N - x, x, y)
        findWinner(N - y, x, y)


arr = [int(i) for i in input().strip().split()]
N = arr[0]
x = arr[1]
y = arr[2]
print(findWinner(N, x, y))
