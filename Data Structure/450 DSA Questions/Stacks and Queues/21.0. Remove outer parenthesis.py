# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
def removeOuterParentheses(S):
    cnt = 0
    res = ''
    for c in S:
        if c == ')':
            cnt -= 1

        if cnt != 0:
            res += c

        if c == '(':
            cnt += 1
    return res
