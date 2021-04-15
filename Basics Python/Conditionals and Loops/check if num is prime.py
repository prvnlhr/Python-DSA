def checkPrime(n):
    isPrime = ''
    for i in range(2, n):
        if (n % i == 0):
            isPrime = 'Not Prime'
            break
        else:
            isPrime = "Prime"
    return isPrime


n = int(input())
ans = checkPrime(n)
print(ans)
