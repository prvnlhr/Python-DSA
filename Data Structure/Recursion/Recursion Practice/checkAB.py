def checkAB(str):
    if len(str) == 0:
        return 'true'
    if (str[0] == 'a'):
        if (len(str[1:]) > 1 and str[1:3] == 'bb'):
            return checkAB(str[3:])
        else:
            return checkAB(str[1:])
    else:
        return 'false'


str = input()
print(checkAB(str))
