def twoSum(nums, target):
    # n = len(nums)
    # for i in range(n):
    #     for j in range( i+1, n):
    #         if(nums[i] + nums[j]==target):
    #             return (i , j)

    i = 0
    j = len(nums) - 1
    while i < j:

        if (nums[i] + nums[j] == target):
            print(i, j)
        elif (nums[i] + nums[j] > target):
            j = j - 1
        elif (nums[i] + nums[j] < target):
            i = i + 1


nums = [int(i) for i in input().split()]
target = int(input())
twoSum(nums, target)
# print(i, j)
