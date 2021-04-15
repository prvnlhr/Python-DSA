def reverseEachWord(str):
    startIndex = 0
    str = str + " "
    endIndex = 0
    newStr = ''
    l = len(str)
    print(l)
    for i in range(len(str)):
        if (str[i] == ' '):
            startIndex = (i - l) - 1
            if (endIndex == 0):
                temp = str[startIndex::-1]
            else:
                temp = str[startIndex:endIndex:-1]
            newStr = newStr + temp + " "
            endIndex = i
    return newStr


str = input()

ans = reverseEachWord(str)
print(ans)
