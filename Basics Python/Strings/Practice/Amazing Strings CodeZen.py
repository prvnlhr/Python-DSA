# def isPresent(currChar, s):
#     if (len(s) == 1 and s[0] != currChar):
#         return False
#     if (s[0] == currChar):
#         return True
#     return isPresent(currChar, s[1:])
#
#
# def AmazingStrings(first, second, third):
#     f = len(first)
#     s = len(second)
#     t = len(third)
#     if (t != (s + f)):
#         return 'NO'
#     for i in range(len(third)):
#         currChar = third[i]
#         ans1 = isPresent(currChar, first)
#         if (ans1 == False):
#             ans2 = isPresent(currChar, second)
#             if (ans2 == False):
#                 return "NO"
def findAscii(s):
    val = 0
    for i in range(len(s)):
        val = val + ord(s[i])
    return val


def AmazingStrings(first ,second ,third):
    f = len(first)
    s = len(second)
    t = len(third)
    if (t != (s + f)):
        return 'NO'
    val1 = findAscii(first)
    val2 = findAscii(second)
    val3 = findAscii(third)
    if(val3 == (val1+val2)):
        return "YES"
    else:
        return "NO"



first = input()
second = input()
third = input()
print(AmazingStrings(first, second, third))
