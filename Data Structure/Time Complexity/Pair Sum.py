def pairSum1(arr, x):
    arr1  = sorted(arr)
    print(arr1)
    l = len(arr1)
    i = 0
    j = len(arr1) - 1
    k = 0
    count = 0
    while i < j :
        if ((arr1[i] + arr1[j])==x):
            count = count +1
            # print(arr1[i] , arr1[j])
            i = i + 1
        if ((arr1[i] + arr1[j]) > x):
            j = j - 1


def pairSum(arr, x):
    arr1  = sorted(arr)
    l = len(arr1)
    for i in range(l):
        for j in range(i+1 , l):
            if (arr1[i] + arr1[j] ==x):
                print(arr1[i] , arr1[j])





# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)
