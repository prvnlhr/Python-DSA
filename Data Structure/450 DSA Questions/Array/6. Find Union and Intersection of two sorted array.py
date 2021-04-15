def intersection(arr1, arr2):
    i = 0
    j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i = i + 1
        elif (arr1[i] > arr2[j]):
            arr.append(arr2[j])
            j = j + 1
        else:
            arr.append(arr1[i])
            i = i + 1
            j = j + 1
    while i < len(arr1):
        arr.append(arr1[i])
        i = i + 1
    while j < len(arr2):
        arr.append(arr2[j])
        j = j + 1
    return arr


arr1 = [int(i) for i in input().strip().split()]
arr2 = [int(j) for j in input().strip().split()]

ans = intersection(arr1, arr2)
print(ans)
