# goes TLE
def intersection(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    l1 = len(arr1)
    l2 = len(arr2)
    if l1 == 0 or l2 == 0:
        return

    if arr1[0] < arr2[0]:
        intersection(arr1[1:], arr2)
    if arr1[0] > arr2[0]:
        intersection(arr1, arr2[1:])
    if arr1[0] == arr2[0]:
        print(arr1[0])
        intersection(arr1[1:], arr2[1:])

# _______________________________________________________
# fast solution
def Aintersection(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    l1 = len(arr1)
    l2 = len(arr2)
    i = 0
    j = 0
    while (i != l1 and j != l2):

        if arr1[i] == arr2[j]:
            print(arr1[i])
            i = i + 1
            j = j + 1

        elif arr1[i] > arr2[j]:
            j = j + 1

        else:
            i = i + 1

# ________________________--main
n = int(input())
arr1 = [int(i) for i in input().strip().split()]
m = int(input())
arr2 = [int(j) for j in input().strip().split()]
intersection(arr1, arr2)
# arr1 = sorted(arr1)
#     print(arr1)
#     print(arr2)
#     arr2 = sorted(arr2)
