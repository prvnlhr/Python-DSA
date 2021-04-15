

def digitSum(n):

    if n==0:
        return 0

    lastval = n%10
    ans = lastval + digitSum(n//10)
    return ans



n = int(input())
print(digitSum(n))
