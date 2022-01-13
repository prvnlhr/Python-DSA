import sys
from heapq import *


# 1. Initialize next array(pointers) with all 0's.
# 2. (finding the minimum value iteratively at every step)Find the indices
#    of the lists containing the minimum(min(i) and the maximum(max(i))
#    elements amongst the elements pointed by the next array.
# 3. If the range formed by the maximum and minimum elements found above
#    is larger than the previous maximum range, update the boundary values used for the maximum range.
# 4. Increment the pointer nums[min(i)]
# 5. Repeat steps 2 to 4 till any of the lists gets exhausted.
#
# To avoid this iterative process, a better idea is to make use of a Min-Heap,
# which stores the values being pointed currently by the next array.
# Thus, the minimum value always lies at the top of this heap, and we
# need not do the iterative search process.

class Solution:
    # At every step, we remove the minimum element from this heap and find
    # out the range formed by the current maximum and minimum values, and compare it
    # with the minimum range found so far to determine the required
    # minimum range.We also update the increment the index in next
    # corresponding to the list containing this minimum entry and add this
    # element to the heap as well.

    def smallestInRange(self, nums):

        # STEP 1: Maintain minHeap and MIN and MAX value for tracking range
        minHeap = []
        MIN = sys.maxsize
        MAX = -sys.maxsize

        # STEP 2: Put all the first elements from all list along with i,j position into heap
        # also update MIN and MAX value
        for i, arr in enumerate(nums):
            heappush(minHeap, (arr[0], i, 0))
            MIN = min(MIN, arr[0])
            MAX = max(MAX, arr[0])

        # res stores range start and end
        res = [MIN, MAX]
        # range to store range difference
        range = MAX - MIN
        max_end = MAX

        # STEP 3:
        # till heap does not exhaust,
        # pop element from minHeap,which will give minValue

        while minHeap:

            val, i, j = heappop(minHeap)  # pop element from minHeap , which will give minValue
            next_index = j + 1
            # if next_index does not exist in pop element's list, i.e list exhausted,return res
            if next_index >= len(nums[i]):
                return res

            # if next_index exists, push to minHeap
            heappush(minHeap, (nums[i][next_index], i, next_index))

            # now compare new_range from previous range formed from MIN ,MAX
            new_min = minHeap[0][0]
            max_end = max(max_end, nums[i][next_index])

            new_range = max_end - new_min
            # if new_range is smaller then old range update and update res
            if new_range < range:
                res = [new_min, max_end]
                range = new_range

        return res


obj = Solution()

# matrix = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
matrix = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
k = 3
ans = obj.smallestInRange(matrix)
print(ans)
