# Is Based on The Approach of Graph
# This Problem has many solution based on Graph, Two-pointer,Stack
# Stack Sol is O(N) and O(N)
# Two Pointer sol are of Two types: 1) O(n ^ 2) 2) O(n) and O(1)
#
#

# O(n) and O(1)
def findCelebrity(n, mat):
    start = 0
    end = n - 1
    # this loop find a potential candidate which can be celebrity
    while start < end:
        if mat[start][end] == 1:
            start = start + 1
        else:
            end = end - 1
    candidate = start
    # this loop finally , check if candidate is celebrity or not
    for i in range(n):
        if i != candidate and (mat[candidate][i] == 1 or mat[i][candidate] == 0):
            return -1
    return candidate


n = int(input())
mat = [[int(j) for j in input().strip().split()] for i in range(n)]
print(findCelebrity(n, mat))
