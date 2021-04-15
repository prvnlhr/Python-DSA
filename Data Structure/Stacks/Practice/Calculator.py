def calculate(s):
    stack = []
    curr = 0
    ans = 0
    while curr < len(s):
        # print(s[curr])
        if s[curr] != '+' and s[curr] != '-' and s[curr] != '(' and s[curr] != ')' and len(stack) != 0:
            currentNum = int(s[curr])
            currentSign = stack[-1]
            if currentSign == '+':
                ans = ans + currentNum
                stack.pop()
            elif currentSign == '-':
                ans = ans - currentNum
                stack.pop()
        elif 0 <= int(s[curr]) <= 9:
            stack.append(s[curr])
        curr = curr + 1
    print(stack, ans)


s = input()
print(calculate(s))
