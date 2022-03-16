"""
https://leetcode.com/problems/spiral-matrix/
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # 4 POINTERS: top, bottom, left, right
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        MAX_STEPS = num_rows * num_cols
        num_steps = 0

        top = 0
        bottom = num_rows - 1
        left = 0
        right = num_cols - 1

        order = []

        while top <= bottom and left <= right:

            # top row
            for col in range(left, right + 1):
                value = matrix[top][col]
                order.append(value)
                num_steps = num_steps + 1

            top = top + 1  # increment row
            if num_steps == MAX_STEPS:
                break

            # right column
            for row in range(top, bottom + 1):
                value = matrix[row][right]
                order.append(value)
                num_steps = num_steps + 1

            right = right - 1
            if num_steps == MAX_STEPS:
                break

            # bottom row (reverse)
            for col in range(right, left - 1, -1):
                value = matrix[bottom][col]
                order.append(value)
                num_steps = num_steps + 1

            bottom = bottom - 1
            if num_steps == MAX_STEPS:
                break

            # left column (reverse)
            for row in range(bottom, top - 1, -1):
                value = matrix[row][left]
                order.append(value)
                num_steps = num_steps + 1

            left = left + 1
            if num_steps == MAX_STEPS:
                break

        return order
