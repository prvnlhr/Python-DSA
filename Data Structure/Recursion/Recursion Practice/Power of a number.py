
def power( x , n):

    if(n==0):
        return 0

    if(n==1):
        return x

    ans = power(x , n-1)
    return  ans * x






x = int(input())
n = int(input())
print(power(x , n))
