import queue


def checkBalanced(expr):
    stack = []

    for char in expr:
        if char in '({[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()

    if not stack:
        return True
    return False


exp = input()
if checkBalanced(exp):
    print('true')
else:
    print('false')
