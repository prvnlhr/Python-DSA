def removeChar(str, char):
    newStr = ""
    for i in range(len(str)):
        if (str[i] == char):
            continue

        newStr = newStr + str[i]

    return newStr


str = input()
char = input()
ans = removeChar(str, char)
print(ans)
