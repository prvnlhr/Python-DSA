
def checkPermutation(S , T):
    if(len(S) != len(T)):
        return 'false'
    else:
        val1 = getAscii(S)
        val2 = getAscii(T)
    if(val1 == val2):
        return 'true'
    else:
        return 'false'


def getAscii(str):
    asciiVal = 0
    for i in range(len(str)):
        asciiVal = asciiVal + ord(str[i])
    return asciiVal





S = input()
T = input()
ans = checkPermutation(S,T)
print(ans)
