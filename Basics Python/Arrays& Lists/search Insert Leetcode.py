def searchInsert(nums, target):
    flag = False

    if target == 0:
        return 0
    for i in range(len(nums)):

        if nums[i] == target:
            flag = True
            return i
        if i + 1 < len(nums):

            if target > nums[i] and target < nums[i + 1]:
                flag = True
                return i + 1

    if flag == False and target > nums[len(nums)-1]:
        return len(nums)
    elif flag == False and target < nums[1]:
        return 0


arr = [int(i) for i in input().strip().split()]
target = int(input())
ans = searchInsert(arr, target)
print(ans)
