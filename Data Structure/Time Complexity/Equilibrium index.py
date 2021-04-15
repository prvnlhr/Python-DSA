
def equilibriumIndex(arr):
    TS = 0

    l = len(arr)
    for i in range(l):
        TS = TS + arr[i]
    i = 0
    LS = 0
    RS = 0
    while i < l:
        LS = LS + arr[i]
        RS = TS - (LS - arr[i])

        if RS == LS:
            return i
        i = i + 1


# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print("index", equilibriumIndex(arr))
