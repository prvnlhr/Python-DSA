# CN SOl___
def maxFreq(l):
    d = dict()
    for i in l:
        if i in d:
            d[i] = d.get(i, 0) + 1
        else:
            d[i] = 1
    max = -1
    for x in l:
        if d[x] > max:
            max = d[x]
            num = x

    return num


# ______________________________________________________________
# my sol: Doesnt works for similar frequency elements
def maxFreq(arr):
    d = {}
    max = -1
    maxfreq = -1
    index = len(arr)
    for i in range(len(arr)):
        ele = arr[i]
        if not ele in d:
            d[ele] = 1
        else:
            d[ele] = d[ele] + 1
            if d[ele] >= maxfreq:
                maxfreq = d[ele]
                max = ele

    return max


n = int(input())
arr = [int(i) for i in input().strip().split()]
print(maxFreq(arr))
