# Cant find A naive Solution
# Only found a efficient HashMap Solution:

def highestOccuringChar(str):
    map = {}
    maxFreq = 0
    maxElement =str[0]
    for i in range(len(str)):
        if (str[i] in map):
            map[str[i]] += 1
            currElementFrequency = map[str[i]]
            if (currElementFrequency > maxFreq):
                maxFreq = currElementFrequency
                maxElement = str[i]
        else:
            map[str[i]] = 1

    for i in str:
        if( map[i] == map[maxElement] ):
            return i

    # print(map , maxElement)
    return maxElement

str = input()
ans = highestOccuringChar(str)
print(ans)
