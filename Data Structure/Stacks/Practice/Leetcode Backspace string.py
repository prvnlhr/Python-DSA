# self solved 100%
# without using stack
def backSpaceString(S, T):
    # op1 = op1[0:-1]
    # op2 = op2[0:-1]
    op1 = check(S)
    op2 = check(T)
    # print(op1, op2)
    if op1 == op2:
        return True
    else:
        return False


def check(str):
    ans = ''
    curr = 0
    while curr < len(str):
        # print(str[curr], ans)

        if str[curr] == '#':
            ans = ans[0:-1]
            curr = curr + 1
        else:
            ans = ans + str[curr]
            curr = curr + 1
    return ans


# using stack
# Time:O(N+M) and Space:O(N+M)
def backSpaceStringUsingStack(S, T):
    stack1 = []
    stack2 = []
    op1 = check(S, stack1)
    op2 = check(T, stack2)
    return op1 == op2


def check(str, stack):
    curr = 0
    while curr < len(str):
        if str[curr] == '#' and len(stack) != 0:
            stack.pop()
        elif str[curr] != '#':
            stack.append(str[curr])
        curr = curr + 1

    return ''.join(stack)

# third sol LeetCode O(N+M) and O(1):

S = input()
S = input()
S = input()
S = input()
S = input()
S = input()
S = input()
S = input()
T = input()
# print(backSpaceString(S, T))
print(backSpaceStringUsingStack(S, T))

# Note: Adding two numbers
x = int(input())



# Main_______________________________________________________
