def isBracketsBalanced(str):
    stack = []

    l = len(str)
    isBalanced = False
    for i in range(l):

        if (str[i] == '('):
            stack.append(str[i])
        elif (str[i] == ')'):
            if (len(stack) > 0):
                element = stack.pop()
                if (element == ')'):
                    True
    # print(stack)
    newLen = len(stack)
    # print(newLen)
    if (len(stack) > 0):
        return 'false'
    else:
        return 'true'

str = input()
ans = isBracketsBalanced(str)
print(ans)
