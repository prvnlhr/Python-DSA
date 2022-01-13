# Refer youtube coding ninjas video for more details

# Optimize Solution O(n)::
from sys import stdin


def minimumSumArray(arr, n, k):
    print(n)
    print(len(arr))
    # compute the sum of first k elements
    minimum_sum = 0
    for i in range(k):
        minimum_sum = minimum_sum + arr[i]

    curr_win_sum = minimum_sum

    for j in range(k, n):
        print(j, k, n)
        curr_win_sum += arr[j] - arr[j - k]
        minimum_sum = min(curr_win_sum, minimum_sum)

    print(minimum_sum)


def minimumSusmArray(arr, k):
    # compute the sum of first k elements
    minimum_sum = 0
    for i in range(k):
        minimum_sum = minimum_sum + arr[i]

    curr_win_sum = minimum_sum
    min_array_index = k - 1

    for j in range(k, len(arr)):
        # removing element from window
        curr_win_sum = curr_win_sum - arr[j - k]
        # adding new element in window
        curr_win_sum = curr_win_sum + arr[j]
        # if curr_win_sum is smaller update  minimum sum::
        # print("before", curr_win_sum, minimum_sum, min_array_index)
        minimum_sum = min(curr_win_sum, minimum_sum)
        # if curr_win_sum < minimum_sum:
        #     minimum_sum = curr_win_sum
        #     min_array_index = j
        # print("after", curr_win_sum, minimum_sum, min_array_index)

    startIndex = min_array_index - k + 1
    endIndex = min_array_index
    print(minimum_sum)
    for i in range(min_array_index - k + 1, min_array_index + 1):
        print(arr[i], end=' ')


# n_k = list(map(int, stdin.readline().strip().split("  ")))
n_k = [int(i) for i in input().strip().split()]
n = int(n_k[0])
k = int(n_k[1])
arr = [int(i) for i in input().strip().split()]
minimumSumArray(arr, n, k)
