#
# EX__. [6 3 -1 -3 4 -2 2 4 6 -12 -7]

# subarray from 2 to 4
# subarray from 2 to 6
# subarray from 5 to 6
# subarray from 6 to 9
# subarray from 0 to 10

# map = {
# 6: [0],
# 9: [1, 4, 6],
# 8: [2], 5: [3],
# 7: [5, 9],
# 13: [7],
# 19: [8],
# 0: [10]
# }

# INTUITION:
# 1. Traverse a array and find sum at that point
# 2. check if sum is in map or not
# 3. if not in map ,then append the sum to map and index of that sum
# 4. if sum in map , get [index array] at that sum from map, and iterate over it
# See gfg dry run image for better understanding

def subArraySumToZero(arr):
    map = {}
    output = []
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
        if sum == 0:
            output.append((0, i))

        al = []
        if sum in map:
            al = map[sum]
            for j in range(len(al)):
                output.append((al[j] + 1, i))
        al.append(i)
        map[sum] = al
    return output


arr = [int(i) for i in input().strip().split()]
ans = subArraySumToZero(arr)
for x in ans:
    print('subarray from', x[0], 'to', x[1])
