# steps included in this program are:
# step1-: At first , let say we are at second row and 0th column (loop in printHelper). we will place the queen at this position
# and call isSafe for this position and check all three upper positions as the downward positions are yet to be filled
# we wont check them..if we found this position to be safe then we will return true and mark it as == 1. and
# we will call printHelper for next row and 0th column. but let say we receive false from isSafe we will wont mark it as == 1 but we will
# move to next col position.
# So basically for every row we are check every col positions if it is safe or not. if safe we move to next row for
# next queen otherwise we place queen in next col
#
def nQueen(n):
    chess = [[0 for j in range(n)] for i in range(n)]
    printPathHelper(chess, 0, n)


def printPathHelper(chess, row, n):
    #  at end we reach the last row that is we are done placing all queens so we gonna print the path
    # Base Case: Printing:
    if row == n:
        for i in range(n):
            for j in range(n):
                print(chess[i][j], end=" ")
        print()
        return

    # ___________________________________
    for col in range(n):
        if (isSafe(chess, row, col, n) is True):
            # if isSafe returns true then we mark this position as safe and move to next row and check every col by calling printHelper
            # Marking ==1:
            chess[row][col] = 1
            # Calling for next row:
            printPathHelper(chess, row + 1, n)
            # Backtrack:
            chess[row][col] = 0
    return


# _isSafe function:____________________________________________________________________________________________________________________________________________
#  this function checks that for a particular col in row if above three directions(upper left and right diagonals ,vertically straight up) has queen or not
# if safe returns true to printHelper above..
def isSafe(chess, row, col, n):
    # Checking vertically upwards:
    i = row - 1
    j = col
    while i >= 0:
        if chess[i][j] == 1:
            return False
        i = i - 1

    # Checking upper-left diagonal:
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if chess[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    # Checking upper-right diagonal:
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if chess[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True


n = int(input())
nQueen(n)
