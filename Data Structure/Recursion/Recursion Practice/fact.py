
def fact(n):


    if(n==1):
        return 1

    ans = fact(n-1)
    return ans * n


n = int(input())
print(fact(n))
