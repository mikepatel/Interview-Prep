"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Approach 1: TWO POINTERS, dynamic programming
        """
        maximum = -10**4  # from constraints

        for i in range(len(nums)):
            current = nums[i]

            if current > maximum:
                maximum = current

            j = i+1
            while j < len(nums):
                current = current + nums[j]
                j += 1

                if current > maximum:
                    maximum = current

        return maximum
        """

        # Approach 2:
        total = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            # does adding the next number increase the total
            if total + current > current:
                total = total + current

            else:  # adding the next number decreases the total
                total = current  # reset starting point

            if total > maximum:
                maximum = total

        return maximum
