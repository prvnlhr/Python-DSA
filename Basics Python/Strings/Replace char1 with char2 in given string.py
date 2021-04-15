

def replaceChar(str , char1 , char2):
    newStr = ''
    for i in range(len(str)):
        if(str[i] == char1 ):
            newStr = newStr + char2
        else:
            newStr = newStr + str[i]
    return newStr

str = input()
char1 = 'a'
char2 = 'f'

ans = replaceChar(str , char1 ,char2)
print(ans)
