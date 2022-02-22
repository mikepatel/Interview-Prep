"""
https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize
        max_area = 0
        i = 0  # first pointer
        j = len(height) - 1  # second pointer
        areas = []

        # brute force
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         area = (j-i) * min(height[i], height[j])
        #         if area > max_area:
        #             max_area = area

        # two pointers
        while i < j:
            width = j - i

            if height[i] < height[j]:
                area = width * height[i]
                areas.append(area)

                # move left-side pointer
                i += 1

            else:
                area = width * height[j]
                areas.append(area)

                # move right-side pointer
                j = j - 1

        max_area = max(areas)
        return max_area
