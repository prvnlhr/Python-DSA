def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1

    return len(nums)


arr = [int(i) for i in input().strip().split()]
n = len(arr)
n = (removeElement(arr, n))
for i in range(0, n):
    print(arr[i], end=' ')
