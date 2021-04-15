def extractUnique(s):
    ans = ''
    d = {}
    for i in range(len(s)):

        if s[i] in d:
            key = s[i]
            d[key] = d[key] + 1
        else:
            key = s[i]
            ans = ans + s[i]
            # print("key", key)
            d[key] = 1
    # print(d)
    # print(ans)
    return ans


s = input()
print(extractUnique(s))
