

def checkNum(n):
    if(n==0):
        return "Zero"
    if(n <0):
        return "Negative"
    else:
        return "Positive"

n = int(input())
ans  = checkNum(n)
print(ans)
