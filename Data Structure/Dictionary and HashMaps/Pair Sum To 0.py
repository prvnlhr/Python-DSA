# ___My solution works but not passes hidden test cases ____________________________________________________________________________________________________________________
def pairSum(l):
    if len(l) == 2 and l[0] == 0 and l[1] == 0:
        print(l[0], l[0])
        return
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1

    if len(d) == 1:
        return

    for i in d:
        key = -i
        value = d[i]
        if key in d and d[key] > 0:
            while value > 0:
                print(min(key, i), max(key, i))
                d[i] = d[i] - 1
                value = value - 1


# __CN solution____________________________________________________________________________________________________________________
def pairSum0(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    size = len(l)
    # print(d)
    for i in range(size):
        key = l[i]
        if -key in d and d[key] != 0:
            if key == (-key):
                occurence = d[key]
                times = (occurence * (occurence - 1)) // 2

                while times != 0:
                    print(key, key)
                    times = times - 1
                d[key] = 0
                continue
            times = d[key] * d[-key]
            while times != 0:
                print(min(key, -key), max(key, -key))

                times = times - 1
            d[key] = 0
            d[-key] = 0


n = int(input())
l = list(int(i) for i in input().strip().split(' '))
pairSum0(l)
