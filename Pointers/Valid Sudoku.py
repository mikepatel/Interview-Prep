"""
https://leetcode.com/problems/valid-sudoku/
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BRUTE FORCE
        num_rows = len(board)
        num_cols = len(board[0])

        # row validation
        for r in range(num_rows):
            row = board[r]
            row_map = {}

            for c in row:
                if c == ".":
                    continue

                else:
                    if c in row_map:  # seen column value 'c' in current row previously
                        print(row_map)
                        return False

                    else:  # not seen column value 'c' in current row previously
                        row_map[c] = True

        # column validation
        for c in range(num_cols):
            col_map = {}

            for r in range(num_rows):
                value = board[r][c]

                if value == ".":
                    continue

                else:
                    if value in col_map:  # seen 'value' in current column previously
                        return False

                    else:  # not seen 'value' in current column previously
                        col_map[value] = True

        # 3x3 validation
        # 9 squares to check
        r = 0
        c = 0
        while r <= 6:
            while c <= 6:
                # square
                square = {}
                for i in range(3):
                    for j in range(3):
                        value = board[r + i][c + j]

                        if value == ".":
                            continue

                        else:
                            if value in square:  # see 'value' in square previously
                                return False

                            else:  # not seen 'value' in square previously
                                square[value] = True

                # iterate to next square horizontally
                c += 3

            # iterate to next square vertically
            c = 0  # reset column pointer
            r += 3

        return True
