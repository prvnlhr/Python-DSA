# _Factorial Function________________________
def fact(n):
    if n == 0:
        return 1
    res = n * fact(n - 1)
    return res


# Main________________________________
n = int(input())
ans = fact(n)
print(ans)
