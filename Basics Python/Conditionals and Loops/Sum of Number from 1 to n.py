
def sumToNusingWhileLoop(n):
    i = 0
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum

def sumToNusingForLoop(n):
    sum = 0
    # for i in range(start ,end , increment):

    for i in range(n+1):
        sum = sum + i
    return sum


n = int(input())

# ans = sumToNusingWhileLoop(n)
ans = sumToNusingForLoop(n)
print(ans)
