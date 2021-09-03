# Refer youtube coding ninjas video for more details

# Optimize Solution O(n)::
def minimumSumArray(arr, k):
    currWinSum = 0

    for i in range(k):
        currWinSum = currWinSum + arr[i]

    minimumSum = currWinSum
    minArrayIndex = k - 1



    for j in range(k, len(arr)):
        # removing element from window
        currWinSum = currWinSum - arr[j - k]
        # adding new element in window
        currWinSum = currWinSum + arr[j]
        # if currWinSum is smaller update  minimum sum::
        # print("before", currWinSum, minimumSum, minArrayIndex)
        if currWinSum < minimumSum:
            minimumSum = currWinSum
            minArrayIndex = j
            # print("after", currWinSum, minimumSum, minArrayIndex)

    startIndex = minArrayIndex - k + 1
    endIndex = minArrayIndex

    for i in range(minArrayIndex - k + 1, minArrayIndex + 1):
        print(arr[i], end=' ')


arr = [int(i) for i in input().strip().split()]
minimumSumArray(arr, 3)
