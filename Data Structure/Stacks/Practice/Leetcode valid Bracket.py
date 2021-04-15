def isValid(s):
    stack = []
    ans = False
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
            stack.
        else:
            if len(stack) == 0 and len(s) != 0:
                return False
            else:
                ele = stack.pop()
                if ele == '[' and i == ']':
                    ans = True
                elif ele == '(' and i == ')':
                    ans = True
                elif ele == '{' and i == '}':
                    ans = True
                else:
                    return False
    print(len(stack))
    if len(stack) != 0:
        return False
    return ans


# "(){}}{"


s = input()
print(isValid(s))
