"""
https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        rows_to_modify = {}
        cols_to_modify = {}

        # step 1: track which rows/columns need to be modified
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    if i not in rows_to_modify:
                        rows_to_modify[i] = True

                    if j not in cols_to_modify:
                        cols_to_modify[j] = True

        # step 2: perform modification in-place
        for i in range(num_rows):
            for j in range(num_cols):
                if i in rows_to_modify:
                    matrix[i][j] = 0

                if j in cols_to_modify:
                    matrix[i][j] = 0
