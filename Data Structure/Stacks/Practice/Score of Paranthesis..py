def scoreOfParentheses(S):
    curr = 0
    stack = []
    ans = 0
    while curr < len(S):
        if S[curr] == ')':
            if stack and stack[-1] == '(':
                ans = ans + 1
                stack.pop()
        else:
            stack.append(S[curr])
        curr = curr + 1
    return ans


s = input()
print(scoreOfParentheses(s))
