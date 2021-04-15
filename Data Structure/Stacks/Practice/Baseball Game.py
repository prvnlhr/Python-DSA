def calPoints(ops):
    stack = []
    curr = 0
    sum = 0

    while curr < len(ops):
        if ops[curr] == 'C':
            top = stack[-1]
            sum = sum - top
            stack.pop()
        elif ops[curr] == 'D':
            top = stack[-1]
            new = top * 2
            stack.append(new)
            sum = sum + new

        elif ops[curr] == '+':
            x = stack[-1]
            y = stack[-2]
            new = x + y
            stack.append(new)
            sum = sum + new
        else:
            x = ops[curr]
            y = int(x)
            stack.append(y)
            sum = sum + y
        curr = curr + 1
    # print(stack, sum)
    return sum


ops = [i for i in input().strip().split()]
print(ops)
print(calPoints(ops))
