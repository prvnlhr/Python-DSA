# my sol 100%________________
def maxDistance(arr):
    m = {}
    distance = 0

    for i in range(len(arr)):

        if arr[i] in m:
            currDist = i - arr.index(arr[i])
            # print(arr[i], distance, currDist)
            if currDist > distance:
                distance = currDist
        else:
            ele = arr[i]
            m[ele] = i
    # print(m)
    return distance


n = int(input())
arr = [int(i) for i in input().strip().split()]
print(maxDistance(arr))
