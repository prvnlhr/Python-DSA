def movePositiveToEnd(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        print(arr[i], arr[j])
        # both value are negative
        if (arr[i] < 0 and arr[j] < 0):
            print("i++")
            i = i + 1
        #  positive and negative
        elif (arr[i] > 0 and arr[j] < 0):
            arr[i], arr[j] = arr[j], arr[i]
            print("swap")
            i = i + 1
            j = j - 1
        # both values are positive
        elif (arr[i] > 0 and arr[j] > 0):
            print("j++")
            j = j - 1
        # negative and positive
        elif (arr[i] < 0 and arr[j] > 0):
            print("i++ , j++")
            i = i + 1
            j = j - 1
    return arr


arr = [int(i) for i in input().strip().split()]

ans = movePositiveToEnd(arr)
print(ans)
