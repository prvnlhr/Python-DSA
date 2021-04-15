def removeElement(nums, val):
    n = len(nums)
    nums = sorted(nums)
    s = n - 1
    count = 0
    for i in range(n):
        if nums[i] == val:
            nums[i] = nums[s]
            s = s - 1
            count = count + 1
    nums = nums
    print(nums)
    arr = nums
    nums = arr
    return n - count


nums = [int(i) for i in input().strip().split()]
val = int(input())
n = removeElement(nums, val)
for i in range(n):
    print(nums[i], end=' ')
