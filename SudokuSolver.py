class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def isSafe(row, col, digit):
            box_id = (row // 3) * 3 + (col // 3)
            return (
                digit not in rows[row]
                and digit not in cols[col]
                and digit not in boxes[box_id]
            )

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

                    box_id = (row // 3) * 3 + (col // 3)

                    board[row][col] = digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[box_id].add(digit)

                    if halperFunction(nextRow, nextCol):
                        return True
                    board[row][col] = "."
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    boxes[box_id].remove(digit)

            return False

        halperFunction(0, 0)
