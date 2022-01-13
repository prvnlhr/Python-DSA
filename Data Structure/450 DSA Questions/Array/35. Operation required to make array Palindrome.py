# Ex__1. 6 1 4 3 1 7

# Steps:
#     6 1 4 3 1 7
#     |         |
#     i         j
# if arr[i] == arr[j] , i=i+1 , j=j-1
# if arr[i] < arr[j] , arr[i+1] = arr[i+1] + arr[i] , i = i + 1,merge
# if arr[i] > arr[j],arr[j - 1] = arr[j - 1] + arr[j] , j = j - 1 ,merge
# Dry run
#  6 1 4 3 1 7
# i = 0 , 6 < 7 --> 1 = 6 + 1 = 7 ,so,after merging 6,1 together --> 7 4 3 1 7
# i = 1 , 7 == 7 --> i = i +1 , j = j -1
# i = 2 , j = 4 , 4 > 1 , 3 + 1 = 4 , so after merging 3,1 together -->  7 4 4 7
# now array became palindrome


def makeArrayPalindrome(arr):
    i = 0
    j = len(arr) - 1
    count_of_operation = 0
    while i < j:
        if arr[i] == arr[j]:
            i = i + 1
            j = j - 1
        elif arr[i] < arr[j]:
            arr[i + 1] = arr[i + 1] + arr[i]
            i = i + 1
            count_of_operation = count_of_operation + 1

        elif arr[i] > arr[j]:
            arr[j - 1] = arr[j - 1] + arr[j]
            j = j - 1

    return count_of_operation


arr = [int(i) for i in input().strip().split()]
ans = makeArrayPalindrome(arr)
print(arr)
