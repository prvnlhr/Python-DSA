

def checkPalindromeRec(str):


    l = len(str)
    if(l==1):
        return 'true'

    if(str[0] != str[l-1]):
        return 'false'
    else:
        checkPalindromeRec(str[1:l-1])
    return 'true'






str = input()
print(checkPalindromeRec(str))
