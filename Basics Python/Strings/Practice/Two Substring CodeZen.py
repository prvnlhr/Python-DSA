def checkTwoSubstring(s):
    return checkTwoSubstringsHelper(s, 0)

def checkTwoSubstringsHelper(s, temp):
    if (len(s) <= 1):
        return 'no'
    if (temp == 0 and s[0] == 'A' and s[1] == 'B'):
        return checkTwoSubstringsHelper(s[2:], 1)
    elif (temp == 0 and s[0] == 'B' and s[1] == 'A'):
        return checkTwoSubstringsHelper(s[2:], 2)
    elif (temp == 1 and s[0] == 'B' and s[1] == 'A'):
        return 'yes'
    elif (temp == 2 and s[0] == 'A' and s[1] == 'B'):
        return 'yes'
    return checkTwoSubstringsHelper(s[1:], temp)


s = input()
print(checkTwoSubstring(s))
