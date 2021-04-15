def findUnique(arr, n):
    for i in range(n):
        print("check for:", arr[i])
        j = 0
        while j < n:
            if (i != j):
                if (arr[i] == arr[j]):
                    print("duplicate found", arr[i], arr[j])
                    break
            j = j + 1
        if (j == n):
            return arr[i]
    return 0

n = int(input())
arr = [int(i) for i in input().split()]
print(findUnique(arr, n))

