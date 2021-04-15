def removeDuplicates(S):
    curr = 0
    stack = []
    stack.append(S[0])
    curr = 1
    while curr < len(S):
        element = S[curr]
        if stack and stack[-1] == element:
            stack.pop()
        else:
            stack.append(element)
        curr = curr + 1

    return ''.join(stack)






s = input()
ans = removeDuplicates(s)
print(ans)
