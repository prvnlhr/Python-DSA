



# without using stack:
# we maintain a counter which tells us weather the outer brackets are
# matched or not. At that point we gonna take a the in between bracket
# and append them to ans
def removeOuterParanthesis(S):
    S2 = ''
    counter = 0
    start = 0
    for i in range(len(S)):
        if S[i] == '(':
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            S2 += S[start+1:i]
            max_num = 0
            start = i + 1
    return S2
# using stack
def removeOuterParentheses(self, S: str) -> str:
        stack = []
        output = []

        for c in S:
            if c == '(':
                if len(stack) > 0:
                    output.append('(')
                stack.append(c)
            else:
                if len(stack) > 1:
                    output.append(')')
                stack.pop()
        return "".join(output)
s  = input()
print(removeOuterParanthesis(s))
