# Python3 program to check whether
# given sudoku board is valid or not

# Checks whether there is any
# duplicate in current row or not
def notInRow(board, row):
    # Set to store characters seen so far.
    st = set()

    for i in range(0, 9):

        # If already encountered before,
        # return false
        if board[row][i] in st:
            return False

        # If it is not an empty cell, insert value
        # at the current cell in the set
        if board[row][i] != 0:
            st.add(board[row][i])

    return True


# Checks whether there is any
# duplicate in current column or not.
def notInCol(board, col):
    st = set()

    for i in range(0, 9):

        # If already encountered before,
        # return false
        if board[i][col] in st:
            return False

        # If it is not an empty cell, insert
        # value at the current cell in the set
        if board[i][col] != 0:
            st.add(board[i][col])

    return True


# Checks whether there is any duplicate
# in current 3x3 box or not.
def notInBox(board, startRow, startCol):
    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = board[row + startRow][col + startCol]

            # If already encountered before,
            # return false
            if curr in st:
                return False

            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != 0:
                st.add(curr)

    return True


# Checks whether current row and current
# column and current 3x3 box is valid or not
def isValid(board, row, col):
    return (notInRow(board, row) and notInCol(board, col) and notInBox(board, row - row % 3, col - col % 3))


def solveSudoku(board):

    for i in range(9):
        for j in range(9):

            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not isValid(board, i, j):
                return False

    return True


board = [[int(ele) for ele in input().split()] for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
