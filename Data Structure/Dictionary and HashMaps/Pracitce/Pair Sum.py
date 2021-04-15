from sys import stdin

# function to print pairs
def printPairs(arr, n, num):
    m = {}
    for i in range(n):
        temp = num - arr[i]
        if num - arr[i] in m:
            count = m[temp]
            for j in range(count):
                print("(", temp, ", ", arr[i], ")", sep="", end='\n')
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

#function to count pair
# my sol correct 100%:
def pairSum(arr, n, num):
    m = {}
    pairCount = 0

    for i in arr:
        ele = i
        if num - i in m:
            pairCount = pairCount + m[num - i]
        if ele in m:
            # Note: don't use m[i] it gives keyError
            # instead use m[ele] where ele = i
            m[ele] = m[ele] + 1
        else:
            m[ele] = 1

    return pairCount


# taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1
