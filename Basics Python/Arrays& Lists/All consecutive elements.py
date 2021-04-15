
def AllCOnsecutives(arr ,n):

    arr.sort()
    flag = 'false'
    print(arr)


    for i in range(1 ,len(arr)):
        # print(arr[i] , arr[i-1]+1)
        if(arr[i] == arr[i-1]+1):
            flag = 'true'
        else:
            flag = 'false'
    return flag









# n = int(input()
N = input()
n = int(N[0])
# list  = [ int(i) for i in range(1 , len(n)).]
# arr = [int(i) for i in input().split()]
arr = [int(N) for x in range(1,n)]
print(n , arr)
print(AllCOnsecutives(arr ,n))
