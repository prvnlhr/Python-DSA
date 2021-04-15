def reverse(n):
    rev = 0
    while (n > 0):
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    return rev



def checkPlaindrome(n):
    rev = reverse(n)
    if(n == rev):
        return 'true'
    else:
        return 'false'

n  = int(input())
print(checkPlaindrome(n))
