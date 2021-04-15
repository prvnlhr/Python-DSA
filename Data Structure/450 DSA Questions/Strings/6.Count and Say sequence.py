def countAndSay(n):
    # ___GeeksForGeeks solution
    # if n == 1:
    #     return '1'
    # if n == 2:
    #     return '11'
    #
    # s = '11'
    #
    # for i in range(3, n + 1):
    #     s = s + '$'
    #     l = len(s)
    #
    #     count = 1
    #     temp = ''
    #     for j in range(1, l):
    #
    #         if (s[j] != s[j - 1]):
    #             temp = temp + str(count + 0)
    #             temp = temp + s[j - 1]
    #             count = 1
    #         else:
    #             count = count + 1
    #
    #     s = temp
    # return s

#_self solved after too much thinking:
    if n == 1:
        return '1'

    s = countAndSay(n - 1)

    count = 1
    temp = ''
    i = 1

    while i < len(s) + 1:
        if i < len(s) and s[i] == s[i - 1]:
            count = count + 1
        else:
            temp = temp + str(count) + str(s[i - 1])
            count = 1
        i = i + 1
    return temp


n = int(input())
ans = countAndSay(n)
print(ans)
