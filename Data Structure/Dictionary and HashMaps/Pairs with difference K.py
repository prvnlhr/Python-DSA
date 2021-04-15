def printPairDiffK(l, k):
    if k<0:
        k*=-1
    m = {}
    for num in l:
        if num + k in m:
            for i in range(0 , m[num+k]):
                print(num , num+k)
        if k!=0 and num - k in m:
            for i in range(0 , m[num-k]):
                print(num-k , num)
        if num in m:
            m[num]+=1
        else:
            m[num] = 1



n = int(input())
l = list(int(i) for i in input().strip().split(' '))
k = int(input())
printPairDiffK(l, k)
