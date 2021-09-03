def convertToTitle(n):
    octalNum = 0
    countVal = 1
    dec = n + 64
    while (dec != 0):
        remainder = dec % 8
        octalNum += remainder * countVal
        countVal = countVal * 10
        dec //= 8
    print(octalNum)
    print(int(octalNum))


n = int(input())
ans = convertToTitle(n)
print(ans)
