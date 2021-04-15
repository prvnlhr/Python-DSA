# Input:  arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}


def cyclicRotateArray(arr):
    # Storing last element
    x = arr[len(arr) - 1]

    # shifting array elements by one
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    # assigning first element equal to x
    arr[0] = x
    return arr


arr = [int(i) for i in input().strip().split()]
ans = cyclicRotateArray(arr)
print(ans)
