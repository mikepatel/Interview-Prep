"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # APPROACH: STACK
        # append while heights are increasing

        # initialize
        stack = []  # store index AND height: [index, height]
        stack.append([0, heights[0]])
        i = 0
        max_area = heights[0]

        while i < len(heights):
            current_height = heights[i]

            if current_height > stack[-1][1]:  # can keep growing stack
                stack.append([i, current_height])

            elif current_height < stack[-1][1]:  # can no longer grow stack
                while stack and current_height < stack[-1][1]:  # calculate max area
                    last_index, last_height = stack.pop()
                    width = i - last_index
                    max_area = max(max_area, width * last_height)

                # begin again @ current
                stack.append([last_index, current_height])

            # move pointer
            i = i + 1

        # finished iterating, calculate max area again
        while stack:
            last_index, last_height = stack.pop()
            width = i - last_index
            max_area = max(max_area, width * last_height)

        return max_area
