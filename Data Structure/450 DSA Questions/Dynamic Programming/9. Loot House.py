# There are n houses build in a line, each of which contains some value in it.
# A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent
# houses because the owner of the stolen houses will tell his two neighbours left and right side.
# What is the maximum stolen value?
# Example::

# Input: hVal[] = {6, 7, 1, 3, 8, 2, 4}
# Output: 19
# Explanation: The thief will steal 6, 1, 8 and 4 from the house.
#
# Input: hVal[] = {5, 3, 4, 11, 2}
# Output: 16
# Explanation: Thief will steal 5 and 11


# EXPLANATION::
# [ 1, 3, 4, 4, 3, 3, 7, 2, 3, 4, 5, 1 ]
# 1 or 3 ? 3 is bigger, so the robber will go to steal 3
#
# On the third house, the robber will think about whether it’s better to steal only 3 or 1 + 4 = 5.
# The robber will steal 5 as it’s a bigger number. Then the robber will decide if he should steal 5 or 3 + 4 = 7.
# The robber will go for 7 and so on. This notation can be written as below:
#
#  1  3  5  7  8 10 15 15 18 19 23 23
# [ 1, 3, 4, 4, 3, 3, 7, 2, 3, 4, 5, 1 ]

# Notice that since the third house, we’ve compared the nums[i] + nums[i-2] and nums[i-1] in
# order to see which choice could be maximum.



# Recursive solution::
def lootHouseRec(arr, n):
    if (n <= 0):
        return 0
    including_house = arr[n - 1] + lootHouseRec(arr, n - 2)
    excluding_house = lootHouseRec(arr, n - 1)
    return max(including_house, excluding_house)


# Memoization solution::
def lootHouseMemo(arr, n, dp):
    if n <= 0:
        return 0

    if (dp[n] == -1):
        including_house = arr[n - 1] + lootHouseMemo(arr, n - 2, dp)
        excluding_house = lootHouseMemo(arr, n - 1, dp)
        ans = max(including_house, excluding_house)
        dp[n] = ans
        return ans
    else:
        ans = dp[n]
        return ans


# Tabulation::

def lootHouseTab(arr, n, dp):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    # dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
    return dp[n - 1]


def lootHouse(arr):
    n = len(arr)
    dp = [-1] * (len(arr) + 1)
    # return lootHouseRec(arr, n)
    # return lootHouseMemo(arr, n, dp)
    return lootHouseTab(arr, n, dp)


arr = [int(i) for i in input().strip().split()]
ans = lootHouse(arr)
print(ans)
