def OddEvenSum(n):
    oddSum = 0
    evenSum = 0
    while n > 0:
        a = n % 10
        if (a % 2 == 0):
            evenSum = evenSum + a
            n = n // 10
        else:
            oddSum = oddSum + a
            n = n // 10
    print(evenSum, " ", oddSum)


n = int(input())
OddEvenSum(n)
