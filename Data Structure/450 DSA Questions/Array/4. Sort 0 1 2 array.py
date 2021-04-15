# In one numsay pass count number of 0's , 1's, 2's.
# In second pass insert 0 1 and 2 according to counts


def sort012(nums):
    # _________SOL 1
    countZero = 0
    countOne = 0
    countTwo = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            countZero = countZero + 1
        if nums[i] == 1:
            countOne = countOne + 1
        if nums[i] == 2:
            countTwo = countTwo + 1

    for j in range(len(nums)):
        if (countZero > 0):
            nums[j] = 0
            countZero = countZero - 1
        elif (countOne > 0):
            nums[j] = 1
            countOne = countOne - 1
        else:
            nums[j] = 2
            countTwo = countTwo - 1
    return nums
    # ___________SOL 2
    lo = 0
    hi = len(arr) - 1
    mid = 0
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo = lo + 1
            mid = mid + 1
        elif nums[mid] == 1:
            mid = mid + 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi = hi - 1
    return nums


nums = [int(i) for i in input().strip().split()]

ans = sort012(nums)
print(ans)
