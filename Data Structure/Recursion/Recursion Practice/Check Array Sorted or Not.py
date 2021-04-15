import sys
def checkSortedHelper(arr , prev ):
    print(arr)
    if(len(arr)==1):
        return 'true'

    curr = arr[0]
    print(curr , prev)
    if( curr > prev):
        return checkSortedHelper(arr[1:] , curr)
    else:
        return 'false'



def checkSorted(arr):
    prev = ~(sys.maxsize)
    ans = checkSortedHelper(arr , prev)
    return ans


arr = [int(i) for i in input().split() ]
ans = checkSorted(arr)
print(ans)
