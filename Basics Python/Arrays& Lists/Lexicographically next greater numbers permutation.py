def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i = i - 1

    if i >= 0:
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j = j - 1

        nums[i], nums[j] = nums[j], nums[i]

    ans = reverse(nums, i + 1)
    return nums


def reverse(nums, start):
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start = start + 1
        end = end - 1
    return nums

nums = [int(i) for i in input().strip().split()]
ans = nextPermutation(nums)
print(ans)
