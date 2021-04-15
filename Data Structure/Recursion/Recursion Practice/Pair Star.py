new = ''


def pairStar(str):
    global new

    if (len(str) == 1):
        new = new + str
        return

    if (str[1] == str[0]):
        new = new + str[0] + '*'
        pairStar(str[1:])

    else:
        new = new + str[0]
        pairStar(str[1:])
    return new


str = input()
print(pairStar(str))
