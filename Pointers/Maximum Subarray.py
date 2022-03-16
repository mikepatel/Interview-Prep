"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find starting point from which to start summing
        """
        #
        total = nums[0]  # first value
        maximum = nums[0]  # first value

        for i in range(1, len(nums)):
            current = nums[i]

            if total <= 0:
                total = current  # reset total

            else:  # total > 0
                total = total + current

            if total > maximum:
                maximum = total

        return maximum
