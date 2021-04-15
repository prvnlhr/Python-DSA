def checkPalindrome(str):
    reverse = str[::-1]
    if (str == reverse):
        return 'true'
    else:
        return 'false'


def checkPalindromeWithoutUsingSlicing(str):
    l = len(str)
    i = 0
    j = l - 1
    while i < j:
        if (str[i] != str[j]):
            return 'false'
        i = i + 1
        j = j - 1

    return 'true'


str = input()

print(checkPalindromeWithoutUsingSlicing(str))
