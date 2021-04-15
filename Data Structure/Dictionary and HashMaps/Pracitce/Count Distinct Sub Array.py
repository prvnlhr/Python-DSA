# def countDistictSubarray(arr, n):
#     # Count distinct elements in whole array
#     vis = dict()
#     for i in range(n):
#         vis[arr[i]] = 1
#     k = len(vis)
#
#     # Reset the container by removing
#     # all elements
#     vid = dict()
#
#     # Use sliding window concept to find
#     # count of subarrays having k distinct
#     # elements.
#     ans = 0
#     right = 0
#     window = 0
#     for left in range(n):
#
#         while (right < n and window < k):
#
#             if arr[right] in vid.keys():
#                 vid[arr[right]] += 1
#             else:
#                 vid[arr[right]] = 1
#
#             if (vid[arr[right]] == 1):
#                 window += 1
#
#             right += 1
#
#         # If window size equals to array distinct
#         # element size, then update answer
#         if (window == k):
#             ans += (n - right + 1)
#
#             # Decrease the frequency of previous
#         # element for next sliding window
#         vid[arr[left]] -= 1
#
#         # If frequency is zero then decrease
#         # the window size
#         if (vid[arr[left]] == 0):
#             window -= 1
#
#     return ans
#
#
# def check(v):
#     # Storing all digits occurred
#     digits = set()
#
#     # Traversing all the numbers of v
#     for i in range(len(v)):
#
#         # Storing all digits of v[i]
#         d = set()
#
#         while (v[i] != 0):
#             d.add(v[i] % 10)
#             v[i] //= 10
#
#         # Checking whether digits of v[i]
#         # have already occurred
#         for it in d:
#             if it in digits:
#                 return False
#
#         # Inserting digits of v[i] in the set
#         for it in d:
#             digits.add(it)
#
#     return True
#
#
# # Function to count the number
# # subarray with all digits unique
# def numberOfSubarrays(a, n):
#     answer = 0
#
#     # Traverse through all the subarrays
#     for i in range(1, 1 << n):
#
#         # To store elements of this subarray
#         temp = []
#
#         # Generate all subarray
#         # and store it in vector
#         for j in range(n):
#             if (i & (1 << j)):
#                 temp.append(a[j])
#
#         # Check whether this subarray
#         # has all digits unique
#         if (check(temp)):
#             # Increase the count
#             answer += 1
#
#     # Return the count
#     return answer


# Python3 program to find the count
# of subarrays of an Array having all
# unique digits

# Function to obtain
# the mask for any integer
def getmask(val):
    mask = 0

    if val == 0:
        return 1

    while (val):
        d = val % 10;
        mask |= (1 << d)
        val = val // 10

    return mask


# Function to count the number of ways
def countWays(pos, mask, a, n):
    # Subarray must not be empty
    if pos == n:
        if mask > 0:
            return 1
        else:
            return 0

    # If subproblem has been solved
    if dp[pos][mask] != -1:
        return dp[pos][mask]

    count = 0

    # Excluding this element in the subarray
    count = (count +
             countWays(pos + 1, mask, a, n))

    # If there are no common digits
    # then only this element can be included
    if (getmask(a[pos]) & mask) == 0:
        # Calculate the new mask
        # if this element is included
        new_mask = (mask | (getmask(a[pos])))

        count = (count +
                 countWays(pos + 1,
                           new_mask,
                           a, n))

    # Store and return the answer
    dp[pos][mask] = count
    return count


# Function to find the count of
# subarray with all digits unique
def numberOfSubarrays(a, n):
    return countWays(0, 0, a, n)


# Driver Code

n = int(input())
arr = [int(i) for i in input().strip().split()]
rows = 5000
cols = 1100

# Initializing dp
dp = [[-1 for i in range(cols)]
      for j in range(rows)]

print(numberOfSubarrays(arr, n))
