def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False


def getTop(stack):
    top = stack.pop()
    stack.append(top)
    return top


def countBracketsReversals(string):
    if len(string) == 0:
        return 0
    if len(string) % 2 != 0:
        return -1
    stack = list()

    for i in range(len(string)):
        currentChar = string[i]

        if currentChar == '{':
            stack.append(currentChar)
        else:
            if not isEmpty(stack) and getTop(stack) == '{':
                stack.pop()
            else:
                stack.append(currentChar)
    count = 0

    while not isEmpty(stack):
        char1 = stack.pop()
        char2 = stack.pop()

        if char1 != char2:
            count += 2
        else:
            count += 1

    return count


string = input().strip()
print(countBracketsReversals(string))
