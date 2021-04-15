# arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# output = [1, 9]

def mergeInterval(arr):
    # Sorting based on the increasing order
    # of the start intervals
    arr.sort(key=lambda x: x[0])

    merged = []

    for interval in arr:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
ans = mergeInterval(arr)
print(ans)
