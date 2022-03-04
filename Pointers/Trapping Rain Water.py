"""
https://leetcode.com/problems/trapping-rain-water/
"""


class Solution:
    def trap(self, height: List[int]) -> int:

        # TWO POINTERS --> while-loop

        # initialize
        total = 0
        left = 0  # left pointer
        right = len(height) - 1  # right pointer

        max_height_left = 0
        max_height_right = 0

        while left < right:
            current_height_left = height[left]
            current_height_right = height[right]

            # left check
            if current_height_left < current_height_right:
                if current_height_left > max_height_left:
                    max_height_left = current_height_left

                else:  # current_height_left <= max_height_left
                    # add area to total
                    total += max_height_left - current_height_left

                left = left + 1  # move left pointer

            # right check
            else:  # current_height_left <= current_height_right
                if current_height_right > max_height_right:
                    max_height_right = current_height_right

                else:  # current_height_right <= max_height_right
                    # add area to total
                    total += max_height_right - current_height_right

                right = right - 1  # move right pointer

        return total
