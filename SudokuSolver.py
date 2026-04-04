class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isSafe(row, col, digit):
            for ind in range(0, 9):
                if board[row][ind] == digit:
                    return False

            for ind in range(0, 9):
                if board[ind][col] == digit:
                    return False

            StartRow = (row // 3) * 3
            StartCol = (col // 3) * 3

            for r in range(StartRow, StartRow + 3):
                for c in range(StartCol, StartCol + 3):
                    if board[r][c] == digit:
                        return False

            return True

        def halperFunction(row, col):
            if row == 9:
                return True

            nextRow = row
            nextCol = col + 1

            if nextCol == 9:
                nextRow = row + 1
                nextCol = 0

            if board[row][col] != ".":
                return halperFunction(nextRow, nextCol)

            for digit in "123456789":
                if isSafe(row, col, digit):
                    board[row][col] = digit
                    if halperFunction(nextRow, nextCol):
                        return True
                    board[row][col] = "."

            return False

        halperFunction(0, 0)
