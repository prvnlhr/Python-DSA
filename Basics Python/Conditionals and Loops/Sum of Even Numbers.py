

def sumofEvenNumToN(n):
    sum = 0
    for i in range(n+1):
        if(i%2 == 0):
            sum = sum + i
    return sum


n = int(input())

ans = sumofEvenNumToN(n)
print(ans)
