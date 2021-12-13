# Given a gold mine of n * m dimensions. Each field in this mine contains a positive integer
# which is the amount of gold in tons. Initially the miner is at first column but can be
# at any row. He can move only (right->,right up /,right down\) that is from a given cell,
# the miner can move to the cell diagonally up towards the right or right or diagonally down
# towards the right. Find out maximum amount of gold he can collect.


# Steps::
# 1. Initialize dp of same length as mine matrix
# 2. We run two loops to fill dp
# 3. To fill dp at i,j we need three values : mine matrix i,j elements right ,right_up and right_down
# 4. So after we get three values dp[i][j] is max(right,right_up,right_down) + mine matrix [i][j]
# NOTE:: we start cols traversing in reverse  i.e from last col

def goldMine(m, n, mine):
    dp = [[0 for i in range(n)] for j in range(m)]

    for col in range(n - 1, -1, -1):
        for row in range(m):

            # if we are at last col, there will be no right ,so ==0
            if col == n - 1:
                right_of_curr = 0
            else:
                right_of_curr = dp[row][col + 1]

            # if row is 0th and col is last ,we don't have right_up so, == 0
            if row == 0 or col == n - 1:
                right_up_of_curr = 0
            else:
                right_up_of_curr = dp[row - 1][col + 1]

            # if last row and last col, we don't have right_down, so == 0
            if row == m - 1 or col == n - 1:
                right_down_of_curr = 0
            else:
                right_down_of_curr = dp[row + 1][col + 1]

            # after getting three values, we fill dp[i][j]
            dp[row][col] = mine[row][col] + max(right_of_curr, right_up_of_curr, right_down_of_curr)

    # print dp
    for i in dp:
        print(i)
    res = dp[0][0]

    # getting final result , which will be maximum of first columns values
    for i in range(1, m):
        res = max(res, dp[i][0])
    # returning the result so obtained
    return res


rows = int(input())
cols = int(input())
mine = [[int(i) for i in input().strip().split()] for j in range(rows)]

print(goldMine(rows, cols, mine))
