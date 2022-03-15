"""
https://leetcode.com/problems/first-missing-positive/
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Approach 1
        # build map
        """
        mapper = {}
        for n in nums:
            if n>0:
                if n not in mapper:
                    mapper[n] = True

        # check if mapper is empty
        if not mapper:
            return 1

        # find missing
        for i in range(1, 2**31):
            if i not in mapper:
                return i
        """

        # Approach 2
        #
        # eliminate all values less than 1
        nums = set(nums)  # eliminate duplicates
        smallest = 1
        for n in nums:
            if n > 0:
                if n == smallest:
                    smallest = smallest + 1

        return smallest

