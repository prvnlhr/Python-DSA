from sys import stdin


def insertionSort(arr, n):
    for i in range(n):
        temp = arr[i]
        j = i - 1
        while j >= 0:
            if (temp < arr[j]):
                arr[j + 1] = arr[j]
            else:
                break
            j = j - 1
        arr[j + 1] = temp


# Input_______________________
# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    insertionSort(arr, n)
    printList(arr, n)

    t -= 1
