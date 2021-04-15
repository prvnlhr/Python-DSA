def maxFreq(l):

    d = {}
    for num in l :
        d[num] = d.get(num , 0) + 1
    # return (max(d, key=lambda key: d[key])) inbuilt function to get key for max value
    max = -2255596634
    maxkey = -88511212
    for i in d:
        if d[i] > max:
            max = d[i]
            maxkey = i
    return maxkey





# Main
n = int(input())
l = list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
