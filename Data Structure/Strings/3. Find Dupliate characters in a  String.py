def findDuplicates(s):
    map = {}

    for i in range(len(s)):
        ele = s[i]
        if s[i] in map:
            map[ele] = map[ele] + 1

            print(s[i], end=' ')
        else:
            map[ele] = 1
    # print(map)


s = input()
ans = findDuplicates(s)
