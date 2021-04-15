# Leetcode
# nums = [1,3,4,2,2]
# output: 2

# SOL 1: sort the array. Repeating elements comes together
# Time O(nLogn) . Needs to modify the array by sorting

# SOL 2: Using map\set:
# Time O(n) and Space(n)

# SOL 3: Floyd's Tortoise and Hare (Cycle Detection)
# Time O(n) . space O(1)
#
#
# _SOL 1:______________________________________________________________
def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]


# _SOL 2:_________________________________________________________________
def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


# _SOL 3:__________________________________________________________________
def findDuplicate(nums):
    # Find the intersection point of the two runners.
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
