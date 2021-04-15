def threeSum(nums):
    n = len(nums)
    sol = []
    # map = {}

    for i in range(n - 1):
        map = {}
        for j in range(i + 1, n):
            x = -(nums[i] + nums[j])
            if x in map:
                # print('ans:', nums[i], nums[j], x)
                ans = [x, nums[j], nums[i]]
                sol.append(ans)
            else:
                # map.add(nums[j])
                map[nums[j]] = 1
    return sol


#
# def findTriplets(nums):
#     n = len(nums)
#     found = False
#     for i in range(n - 1):
#
#         # Find all pairs with sum
#         # equals to "-nums[i]"
#         s = set()
#         for j in range(i + 1, n):
#             x = -(nums[i] + nums[j])
#             if x in s:
#                 print(x, nums[i], nums[j])
#                 found = True
#             else:
#                 s.add(nums[j])
#     if found == False:
#         print("No Triplet Found")

# nums = [int(i) for i in input().strip().split()]
# def threeSum(nums):
#     n = len(nums)
#     sol = []
#     previ = None
#
#     # sort numsay elements
#     nums.sort()
#     for i in range(0, n - 1):
#         if nums[i] == previ:
#             continue
#         previ = nums[i]
#         # initialize left and right
#         l = i + 1
#         r = n - 1
#         x = nums[i]
#         while (l < r):
#
#             if (x + nums[l] + nums[r] == 0):
#                 # print elements if it's sum is zero
#                 sol.append([x, nums[l], nums[r]])
#                 l += 1
#                 r -= 1
#                 break
#
#             # If sum of three elements is less
#             # than zero then increment in left
#             elif (x + nums[l] + nums[r] < 0):
#                 l += 1
#
#             # if sum is greater than zero than
#             # decrement in right side
#             else:
#                 r -= 1
#     return sol

def FindTriplet(arr, x):
    arr1 = sorted(arr)
    l = len(arr1)
    for i in range(0, l - 1):
        st = i + 1
        end = l - 1
        val = x - arr1[i]
        while st < end:
            if (arr1[st] + arr1[end] > val):
                end -= 1
            elif (arr1[st] + arr1[end] < val):
                st += 1
            else:
                count1 = 0
                count2 = 0
                for ptr in range(st, end):
                    if (arr1[ptr] == arr1[st]):
                        count1 += 1
                    else:
                        break
                for ptr in range(end, st, -1):
                    if (arr1[ptr] == arr1[end]):
                        count2 += 1
                    else:
                        break
                comb = count2 * count1
                if (arr1[st] == arr1[end]):
                    comb = ((end - st + 1) * (end - st)) // 2
                for k in range(0, comb):
                    print(arr1[i], end=" ")
                    print(arr1[st], end=" ")
                    print(arr1[end])
                st += 1
                end = end - count2


n = int(input())
arr = [int(y) for y in input().strip().split()]
x = int(input())
FindTriplet(arr, x)

def threeSum(nums):
    def twoSumAgain(index):
        seen = set()
        j = index + 1

        while j < len(nums):
            sum_ = -nums[index] - nums[j]

            # If we have seen the number before, then found the triplet
            if sum_ in seen:
                output.append([nums[index], nums[j], sum_])

                # Avoid all the duplicates
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1

            seen.add(nums[j])
            j += 1

    output = []
    if len(nums) < 3:
        return output

    nums.sort()

    # Anchoring every number
    for i, n in enumerate(nums):
        if nums[i] > 0:
            break

        if i == 0 or nums[i - 1] != nums[i]:
            twoSumAgain(i)

    return output


# nums = [-1, 0, 1, 2, -1, -4]
# [[-1, -1, 2], [-1, 0, 1]]
# nums = [0, -1, 2, -3, 1]
# nums = [-1, 0, 1, 2, -1, -4]
nums = [-2, 0, 0, 2, 2]

# ans = threeSum(nums)
ans = threeSum(nums)
print(ans)
