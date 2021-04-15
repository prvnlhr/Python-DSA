def FindUnique(arr):
    arr1 = sorted(arr)
    print(arr1)
    x = 1
    l = len(arr1)
    for i in range(len(arr1)):
        if arr1[x - 1] != arr1[x]:
            return arr1[x - 1]
        elif x == (l - 2):
            return arr1[l - 1]
        else:
            x = x + 2


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
unique = FindUnique(arr)
print(unique)
